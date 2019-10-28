import numpy as np
import cv2

def detect_faces(f_cascade, colored_img, scaleFactor = 1.1):
    #just making a copy of image passed, so that passed image is not changed
    img_copy = colored_img.copy()
    #convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)       
    #let's detect multiscale (some images may be closer to camera than others) images
    faces = f_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=5);   
    #go over list of faces and draw them as rectangles on original colored img
    for (x, y, w, h) in faces:
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 0, 255), 2)
    return img_copy

#  haar_face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml')
lbp_face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/lbpcascades/lbpcascade_frontalface.xml')

for path in ['/app/MarceloAndrade.png', '/app/2faces.png']:
    img = cv2.imread(path)
    newImg = detect_faces(haar_face_cascade, img)
    newImg = detect_faces(lbp_face_cascade, img)
    cv2.imshow('Test Img', newImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

