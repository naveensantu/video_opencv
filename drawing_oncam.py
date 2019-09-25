import cv2




capture=cv2.VideoCapture(0)

width=int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

x = width // 2
y = height // 2

w = width // 4
h = height // 4


while True:

    ret,frame = capture.read()
    cv2.rectangle(frame,(x,y),(x+w,y+h),color=(0,0,255),thickness=7)
    cv2.imshow("frame",frame)


    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
cv2.destroyAllWindows()
