import cv2

# open camera
cap = cv2.VideoCapture("/dev/jetcocam0")
# check if opened
if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

while True:
    # read frame
    ret, frame = cap.read()
    if not ret:
        print("프레임을 가져올 수 없습니다.")
        break

    # show on screen
    cv2.imshow("Cam", frame)

    # quite when "q" key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    # close can and window
    cap.release()
    cv2.destroyAllWindows()
