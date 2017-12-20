import cv2
import glob

Face_Blue_Print = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

Detect = cv2.imread("Facial//holi-image-4-big.jpg")

cv2.imshow("Loaded",Detect)
cv2.waitKey(0)
cv2.destroyAllWindows()

Detect_Gray = cv2.cvtColor(Detect,cv2.COLOR_BGR2GRAY)

cv2.imshow("Loaded_Grey",Detect_Gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

Faces = Face_Blue_Print.detectMultiScale(Detect_Gray,
                                         scaleFactor = 1.1,
                                         minNeighbors = 5)

print(type(Faces))
print(Faces)

for x,y,w,h in Faces:
    Detect=cv2.rectangle(Detect,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("Loaded",Detect)
cv2.waitKey(0)
cv2.destroyAllWindows()
