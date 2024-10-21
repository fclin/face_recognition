import face_recognition
image = face_recognition.load_image_file("FCLin.png")
face_landmarks_list = face_recognition.face_landmarks(image)

print (face_landmarks_list)