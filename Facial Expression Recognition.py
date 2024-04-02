import cv2
from deepface import DeepFace


model = DeepFace.build_model("Emotion")


cap = cv2.VideoCapture(0)


emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

while True:
    ret, frame = cap.read()

    if ret:
        
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        
        faces = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml').detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

        
        for (x, y, w, h) in faces:
            
            face = frame[y:y+h, x:x+w]

            
            face_resized = cv2.resize(face, (48, 48))

            
            face_gray = cv2.cvtColor(face_resized, cv2.COLOR_BGR2GRAY)

            
            face_normalized = face_gray / 255.0

            
            face_input = face_normalized.reshape(1, 48, 48, 1)

            
            emotion_probs = model.predict(face_input)[0]

            
            predicted_emotion_index = emotion_probs.argmax()

            
            predicted_emotion_label = emotion_labels[predicted_emotion_index]

            
            cv2.putText(frame, predicted_emotion_label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        
        cv2.imshow("Facial Expression Recognition", frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
