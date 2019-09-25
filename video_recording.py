import cv2

capture = cv2.VideoCapture(0)

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter("first_video.mp4",cv2.VideoWriter_fourcc(*'DIVX'),25,(width,height))

while True:
    ret,frame = capture.read()
    writer.write(frame)
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame)

    if cv2.waitKey(delay=1) & 0xFF == 27:
        break
capture.release()
writer.release()
cv2.destroyAllWindows()
