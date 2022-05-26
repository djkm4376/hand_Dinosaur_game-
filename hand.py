from sre_constants import CH_LOCALE
import cv2
import mediapipe as mp
from time import time, sleep
from pywinauto import application 
from multiprocessing import Process
import Chrome_Dinosaur_game

def Hand_Track():
    #손 마디 점찍기
    mp_drawing = mp.solutions.drawing_utils
    #손 인식
    mp_hands = mp.solutions.hands
    #카메라키기
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

                    #검지 엄지거리
                    diff =  thumb.y - index.y

                    
                    volume = int(diff * 500)

                    #검지가 엄지밑으로
                    if volume <= -2:
                        print('웅크리기')
                        
                    #엄지 검지 만남
                    elif volume <= 40:
                        print('달리기')

                    #검지위로
                    elif volume > 40:
                        print('점프')

                    else:
                        print('error')

                    #imshow 에 엄지검지 사이거리 출력
                    cv2.putText(image, text='%d' %(volume), org=(10, 30),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,color=255, thickness=2)

                    #손 랜드마크출력
                    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            cv2.imshow('image', image)

            if cv2.waitKey(1) == ord('q'):
                break
        

        cap.release()

#멀티프로세스 생성자 (손,게임)
if __name__=='__main__':
    t1=Process(target=Hand_Track)
    t2=Process(target=Chrome_Dinosaur_game.game)
    t1.start()
    t2.start()
    t1.join()
    t2.join()