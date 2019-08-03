import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# define circle
color = (0,255,0)
line_width = 3
radius = 100
point = (0,0)

# define mouse callback when button pressed
def click(event, x, y, flags, param):  
	global point, pressed
	if event == cv2.EVENT_LBUTTONDOWN:
		print("Pressed",x,y)
		point = (x,y)

# register event with handler
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",click)  

while(True):
	ret, frame = cap.read()  #reads new frame from capture device

	frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
	cv2.circle(frame, point, radius, color, line_width) #draw the circle
	cv2.imshow("Frame",frame)

	ch = cv2.waitKey(1)  # wait time in milliseconds
	if ch & 0xFF == ord('q'):  # q breaks the loop
		break

cap.release()
cv2.destroyAllWindows()