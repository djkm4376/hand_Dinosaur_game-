import cv2
import mediapipe as mp
from time import time, sleep
from pywinauto import application 

class Hand_Track:

    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    cap = cv2.VideoCapture(0)



    with mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:

        while cap.isOpened():
            success, image = cap.read()
            if not success:
                continue

            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            results = hands.process(image)

            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    thumb = hand_landmarks.landmark[4]
                    index = hand_landmarks.landmark[8]

                    diff = abs(index.x - thumb.x)

                    
                    volume = int(diff * 500)

                    if volume <= 8:
                        print('웅크리기')
                        
                        

                    elif volume <= 40:
                        print('달리기')

                        
                    elif volume <= 100:
                        print('점프')

                    else:
                        print('error')

                    cv2.putText(image, text='%d' %(volume), org=(10, 30),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,color=255, thickness=2)

                    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            cv2.imshow('image', image)

            if cv2.waitKey(1) == ord('q'):
                break
        

        cap.release()

Hand_Track()