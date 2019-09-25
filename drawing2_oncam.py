import cv2

def draw_rect(event,x,y,flags,param):
    global pt1,pt2,topLeft_clicked,bottomRight_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        if topLeft_clicked == True and bottomRight_clicked == True:
            pt1 = (0,0)
            pt2 = (0,0)
            topLeft_clicked = False
            bottomRight_clicked = False

        if topLeft_clicked == False:
            pt1=(x,y)
            topLeft_clicked=True

        elif bottomRight_clicked == False:
            pt2=(x,y)
            bottomRight_clicked=True



pt1 = (0,0)
pt2 = (0,0)
topLeft_clicked = False
bottomRight_clicked = False

capture=cv2.VideoCapture(0)
cv2.namedWindow("test window")
cv2.setMouseCallback("test window",draw_rect)



while True:

    ret,frame = capture.read()
    if topLeft_clicked:
        cv2.circle(frame,center=pt1,radius=5,color=(0,0,255),thickness=-1)

    if topLeft_clicked and bottomRight_clicked:
        cv2.rectangle(frame,pt1,pt2,(0,0,255),3)

    cv2.imshow("test window",frame)


    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
cv2.destroyAllWindows()
