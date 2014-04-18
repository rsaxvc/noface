import cv2

face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_eye.xml')

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

img_circle = cv2.imread("laugh/circle.png", cv2.CV_LOAD_IMAGE_UNCHANGED)
img_face   = cv2.imread("laugh/face.png", cv2.CV_LOAD_IMAGE_UNCHANGED)
img_text   = cv2.imread("laugh/text.png", cv2.CV_LOAD_IMAGE_UNCHANGED)

if vc.isOpened(): # try to get the first frame
	rval, frame = vc.read()
	print "camera"
else:
	rval = False
	print "nocamera"

while rval:
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.1, 4)
	for (x,y,w,h) in faces:
		print "face@",x,y
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	cv2.imshow("preview", frame)
	rval, frame = vc.read()
	key = cv2.waitKey(1)
	if key == 27: # exit on ESC
		break
cv2.destroyWindow("preview")
