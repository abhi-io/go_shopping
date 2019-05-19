
import numpy as np
import cv2,time




import math

while True:
    f = open("x.txt", "r")
    print(f.read())
    time.sleep(0.5)







# p1 = [4, 0]
# p2 = [6, 6]
# distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
#
# print(distance)

# manx1=00
# manx2=00
#
# item1=100
# item2=100
# distance = math.sqrt( ((manx1-item1)**2)+((manx2-item2)**2) )
# print(round(distance))






# cap = cv2.VideoCapture(1,0)
#
#
# while(True):
#     # Capture frame-by-frame
#     time.sleep(0.002)
#     ret, frame = cap.read()
#     fps = cap.get(cv2.CAP_PROP_FPS)
#     print ("Frames per second using cap.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
#
#
#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Display the resulting frame
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()
