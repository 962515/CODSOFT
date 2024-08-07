import face_recognition
import cv2
import os

ajay_image = face_recognition.load_image_file("D:/internship/codsoft/New folder/photos/ajay.jpg")
ajay_encoding = face_recognition.face_encodings(ajay_image)[0]

sakshi_image = face_recognition.load_image_file("D:/internship/codsoft/New folder/photos/sakshi.jpg")
sakshi_encoding = face_recognition.face_encodings(sakshi_image)[0]

arya_image = face_recognition.load_image_file("D:/internship/codsoft/New folder/photos/arya.jpg")
arya_encoding = face_recognition.face_encodings(arya_image)[0]


known_face_encodings = [ajay_encoding, sakshi_encoding, arya_encoding]
known_face_names = ["ajay", "sakshi", "arya"]


video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: Could not open camera.")
    exit()


while True:
    
    ret, frame = video_capture.read()

    if not ret or frame is None:
        print("Failed to capture frame or empty frame. Exiting...")
        break

    
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    
    rgb_small_frame = small_frame[:, :, ::-1]


    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
           first_match_index = matches.index(True)
           name = known_face_names[first_match_index]

        face_names.append(name)

   
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    cv2.imshow("Face Recognition", frame)

    if cv2.getWindowProperty('Face Recognition', cv2.WND_PROP_VISIBLE) < 1:
        print("Window closed by user. Exiting...")
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
