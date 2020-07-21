import cv2

# training the algorithm
trained_face_data = cv2.CascadeClassifier('set.xml')

# reading the image
#img = cv2.imread('bel_selfie.jpg')
webcam = cv2.VideoCapture(0)
# running a loop for each frame
while True:
    succesful_frame_read, frame = webcam.read()
# Converting to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    for (x, y, w, h) in face_coordinates:
        #(x ,y , w, h) = face_coordinates[0]
        # draw rectangles around faces
        cv2.rectangle(grayscaled_img, (x, y), (x+w, y+h), (0, 255, 0), 5)

    cv2.imshow('Clever Programmer Face Detector', grayscaled_img)
    key = cv2.waitKey(1)

    if key == 13:
        break
webcam.release()


"""
#Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)


for (x , y, w ,h) in face_coordinates:
#(x ,y , w, h) = face_coordinates[0]
#draw rectangles around faces
    cv2.rectangle(img, (x,y),(x+w, y+h), (0, 255, 0), 5)






#
cv2.imshow('Clever Programmer Face Detector', img)
cv2.waitKey()

"""


print('CODE COMPLETED!!!')
