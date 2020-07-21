import cv2

#
trained_face_data = cv2.CascadeClassifier('set.xml')
img = cv2.imread('selfie.png')
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
for (x, y, w, h) in face_coordinates:
    #(x ,y , w, h) = face_coordinates[0]
    #draw rectangles around faces
    cv2.rectangle(grayscaled_img, (x, y), (x+w, y+h), (0, 255, 0), 5)
cv2.imshow('Clever Programmer Face Detector', grayscaled_img)
cv2.waitKey()
print('CODE COMPLETED!!!')
