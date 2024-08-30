import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_detection(import_part, export_part):

    img = cv2.imread(import_part)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1, 4)

    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x + w, y + h), (225, 0, 0), 2)

    cv2.imshow('img',img)
    cv2.waitKey()

    cv2.imwrite(export_part, img)

face_detection("test4.jpg", "face_detected4.jpg")

