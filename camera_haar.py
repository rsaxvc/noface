import cv2
import time

face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
	rval, frame = vc.read()
	print "camera"
else:
	rval = False
	print "nocamera"

frames = 0
start_time = time.time()

while rval:
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.1, 4)
	for (x,y,w,h) in faces:
		print "face@",x,y
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

	cv2.imshow("preview", frame)
	rval, frame = vc.read()
	key = cv2.waitKey(1)
	if key == 27: # exit on ESC
		break

	frames += 1
	if( frames % 15 == 0):
		print "AVG FPS:",(frames/(time.time()-start_time))
cv2.destroyWindow("preview")
