import cv2
facesDetect = cv2.CascadeClassifier("Resources/detectfaces.xml")
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    faces = facesDetect.detectMultiScale(img, 1.1, 10)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,255), 2)
        cv2.putText(img, "face", (w, y+h), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 2)

    cv2.imshow("facesDetection", img)
    cv2.waitKey(1)