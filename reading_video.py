import cv2
import time

capture = cv2.VideoCapture('first_video.mp4')

if capture.isOpened() == False:
    print("Error file not found")

while capture.isOpened():
    ret,frame= capture.read()

    if ret == True:
        time.sleep(1/30)
        cv2.imshow("frame",frame)
        if cv2.waitKey(10) & 0xFF == 27:
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()
