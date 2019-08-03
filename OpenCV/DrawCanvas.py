import numpy as np
import cv2

# Global variables
canvas = np.ones([500,500,3],'uint8')*255
radius = 3
color = (0,255,0)
pressed = False # needed for click and hold

# click callback
def click(event, x, y, flags, param):
	global canvas, pressed
	if event == cv2.EVENT_LBUTTONDOWN: # draw a dot
		pressed = True
		cv2.circle(canvas,(x,y),radius,color,-1)  #draw the circle
	elif event == cv2.EVENT_MOUSEMOVE and pressed == True: # continous draw while click and hold
		cv2.circle(canvas,(x,y),radius,color,-1)  #draw the circle
	elif event == cv2.EVENT_LBUTTONUP: # button released
		pressed = False

# register event with handler
# window initialization and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", click)

# Forever draw loop
while True:

	cv2.imshow("canvas",canvas)

	# key capture every 1ms
	ch = cv2.waitKey(1)  # wait time in milliseconds
	if ch & 0xFF == ord('q'):  # q breaks the loop
		break
	elif ch & 0xFF == ord('b'): # Change color if pressed
		color = (255,0,0)
	elif ch & 0xFF == ord('g'):
		color = (0,255,0)
	

cv2.destroyAllWindows()