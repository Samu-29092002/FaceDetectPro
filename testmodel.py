# # pip install opencv-python==4.5.2
# import cv2 
# # from controller import doorAutomate
# # import time

# video=cv2.VideoCapture(0)
# facedetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer.read("Trainer.yml")

# name_list = ["", "sameena","supritha","shahida","sai pallavi","shalini"]

# imgBackground = cv2.imread("background.png")

# while True:
#     ret,frame=video.read()
#     gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = facedetect.detectMultiScale(gray, 1.3, 5)
#     for (x,y,w,h) in faces:
#         serial, conf = recognizer.predict(gray[y:y+h, x:x+w])
#         if conf>50:
#             cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
#             cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
#             # 2
#             cv2.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
#             cv2.putText(frame, name_list[serial], (x, y-40),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
            
#         else:
#             cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
#             cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
#             cv2.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
#             cv2.putText(frame, "Unknown", (x, y-40),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
#     frame=cv2.resize(frame, (640, 480))
#     imgBackground[162:162 + 480, 55:55 + 640] = frame
#     cv2.imshow("Frame",frame)
    
#     k=cv2.waitKey(1)
#     if k==ord("q"):
#         break
# video.release()
# cv2.destroyAllWindows()


import cv2

# Initialize the video capture
video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Load the trained model for face recognition
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("Trainer.yml")

# Define the names list corresponding to labels
name_list = ["", "sameena", "supritha", "shahida", "sai pallavi", "shalini","summayya","altaf"]

# Load the background image if needed
imgBackground = cv2.imread("background.png")

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        serial, conf = recognizer.predict(gray[y:y+h, x:x+w])
        if conf < 70:  # Adjusted condition to recognize known faces
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y-40), (x+w, y), (0, 255, 0), -1)
            cv2.putText(frame, name_list[serial], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        else:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.rectangle(frame, (x, y-40), (x+w, y), (0, 0, 255), -1)
            cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    frame = cv2.resize(frame, (640, 480))
    imgBackground[162:162 + 480, 55:55 + 640] = frame
    cv2.imshow("Frame", frame)
    
    k = cv2.waitKey(1)
    if k == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
