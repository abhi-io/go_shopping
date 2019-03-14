import numpy as np
import cv2
import time

face_cascade = cv2.CascadeClassifier('face.xml') #eye
cap = cv2.VideoCapture(0)
print("loaded")
time.sleep(1)
font = cv2.FONT_HERSHEY_SIMPLEX
bb = ()
subtractor = cv2.createBackgroundSubtractorMOG2(history=20, varThreshold=25, detectShadows=True)
count = 1
while(cap.isOpened()):

	#print("in loop")
	_, frame = cap.read()


	count = count +1
	#cv2.imshow('input frame',frame)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	#print(faces)
	if faces == bb:
		print("not found", count)
		import y
		continue
	for (x,y,w,h) in faces:
		print("**face found**", count)

		img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		cv2.putText(img,' id 1',(x+w,y+h), font, 1,(255,255,255),2,cv2.LINE_AA)
		#cv2.imshow('image*',frame)
		cv2.imshow('image',img)
		if cv2.waitKey(1) == 27:
			break
print("no video")

cap.release()
cv2.destroyAllWindows()
