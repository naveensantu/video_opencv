# * Create a draw_circle function for the callback function
# * Use two events cv2.EVENT_LBUTTONDOWN and cv2.EVENT_LBUTTONUP
# * Use a boolean variable to keep track if the mouse has been clicked up and down based on the events above
# * Use a tuple to keep track of the x and y where the mouse was clicked.
# * You should be able to then draw a circle on the frame based on the x,y coordinates from the Event
#
import cv2

# Create a function based on a CV2 Event (Left button click)

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global center,clicked
    # get mouse click on down and track center
    if event == cv2.EVENT_LBUTTONDOWN:
            center = (x,y)
            clicked = False
    # Use boolean variable to track if the mouse has been released
    if event == cv2.EVENT_LBUTTONUP:
            clicked = True

center = (0,0)
clicked = False
# Capture Video
video=cv2.VideoCapture(0)
# Create a named window for connections
cv2.namedWindow("video assesment")
# Bind draw_rectangle function to mouse cliks
cv2.setMouseCallback("video assesment",draw_circle)


while True:
    # Capture frame-by-frame
    ret,frame = video.read()
    # Use if statement to see if clicked is true
    if clicked == True:
        # Draw circle on frame
        cv2.circle(frame, center, 25, (0,0,255),3)

    # Display the resulting frame
    cv2.imshow("video assesment",frame)

    # This command let's us quit with the "q" button on a keyboard.
    if cv2.waitKey(2) & 0xFF == 27:
        break

video.release()
cv2.destroyAllWindows()
# When everything is done, release the capture
