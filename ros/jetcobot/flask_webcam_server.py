import threading
import time

import cv2
from flask import Flask, Response

app = Flask(__name__)
# latest frame into global variable
FRAME = None
frame_lock = threading.Lock()


def capture_frames():
    global FRAME
    # open camera at /dev/jetcocam0
    camera = cv2.VideoCapture("/dev/jetcocam0")
    if not camera.isOpened():
        print("Cannot open the camera!!!")
        return
    while True:
        success, img = camera.read()
        if not success:
            print("Cannot read the frame!!!")
            time.sleep(0.1)
            continue

        # encode and save frame
        _, buffer = cv2.imencode(".jpg", img)
        with frame_lock:
            FRAME = buffer.tobytes()

        # frame capture rate
        time.sleep(0.03)  # ~30fps


def generate_frames():
    while True:
        # get latest frame
        with frame_lock:

            if FRAME is None:
                time.sleep(0.1)
                continue
            current_frame = FRAME

            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + current_frame + b"\r\n"
            )


@app.route("/stream")
def video_feed():
    return Response(
        generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    capture_thread = threading.Thread(target=capture_frames)
    capture_thread.daemon = True
    capture_thread.start()
    app.run(host="0.0.0.0", port=5000, threaded=True)
