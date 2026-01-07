import threading

import cv2
import numpy as np
import requests


class VideoStreamClient:
    def __init__(self, server_url):
        """
        Initialize video stream client
        Args:
            server_url(str): flask_webcam_server URL : 'http://192.168.0.83:5000/stream'
        """
        self.server_url = server_url
        self.stream_active = False
        self.stream_thread = None
        self.latest_frame = None
        self.frame_lock = threading.Lock()

    def start_stream(self):
        if self.stream_active:
            print("Stream is already active.")
            return
        self.stream_active = True
        self.stream_thread = threading.Thread(target=self._receive_stream)
        self.stream_thread.daemon = True
        self.stream_thread.start()

    def stop_stream(self):
        self.stream_active = False
        if self.stream_thread:
            self.stream_thread.join(timeout=1.0)

    def get_latest_frame(self):
        with self.frame_lock:
            if self.latest_frame is None:
                return None
            return self.latest_frame.copy()

    def _receive_stream(self):
        """internal method takes care of stream input"""
        try:
            # connect to stream
            response = requests.get(self.server_url, stream=True)
            if response.status_code != 200:
                print(f"서버 연결 실패: {response.status_code}")
                self.stream_active = False
                return

            # MJPEG byte date of stream
            bytes_data = bytes()

            # loop to take care of stream
            for chunk in response.iter_content(chunk_size=1024):
                bytes_data += chunk
                a = bytes_data.find(b"\xff\xd8")  # start byte of JPG
                b = bytes_data.find(b"\xff\xd9")  # end bype of JPG

                if a != -1 and b != -1:
                    # get complete JPG frame
                    jpg = bytes_data[a : b + 2]
                    bytes_data = bytes_data[b + 2 :]

                    # JPG byte date into img
                    full_frame = cv2.imdecode(
                        np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR
                    )

                    # store latest frame
                    with self.frame_lock:
                        self.latest_frame = full_frame

                # terminate if stream ends
                if not self.stream_active:
                    break

        except Exception as e:
            print(f"Error while streaming: {e}")
        finally:
            self.stream_active = False


# usage example
if __name__ == "__main__":
    # URL from server
    SERVER_URL = "http://192.168.0.83:5000/stream"

    # construct client and start
    client = VideoStreamClient(SERVER_URL)
    client.start_stream()

    # frame showing loop
    try:
        while True:
            frame = client.get_latest_frame()
            if frame is not None:
                cv2.imshow("Jetcobot Camera Stream", frame)
            # exit when "q" key is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    except KeyboardInterrupt:
        print("terminating...")
    finally:
        client.stop_stream()
        cv2.destroyAllWindows()
