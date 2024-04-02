import cv2
import mediapipe as mp


mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)  


with mp_face_mesh.FaceMesh(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
) as face_mesh:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

       
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

       
        results = face_mesh.process(frame_rgb)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    face_landmarks,
                    mp_face_mesh.FACEMESH_CONTOURS,)
                

        
        cv2.imshow("Face Landmarks Detection", frame)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()
