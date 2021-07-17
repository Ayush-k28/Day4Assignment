import cv2
import mediapipe as mp

mp_drawing=mp.solutions.drawing_utils
mp_hands=mp.solutions.hands
                                            
cap=cv2.VideoCapture(0)   #min_detection_confidence-provides threshold for initial detection & min_tracking_confidence-provides threshold for tracking after detection                                                                                
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        flag,frame=cap.read()
        
        

        results=hands.process(frame)

       
        if results.multi_hand_landmarks:
            for num,hand in enumerate(results.multi_hand_landmarks): #looping through each landmark
                mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
               # mp_drawing.DrawingSpec(color(134,0,255),thickness=2,circle_radius=2),
                #mp_drawing.DrawingSpec(color(0,34,255),thickness=2,circle_radius=2),
                #mp_drawing.DrawingSpec(color(0,34,255),2,2)

        
        cv2.imshow("Frame",frame)
        if cv2.waitKey(10) & 0xff==ord('q'):
            break

        #print(results.multi_hand_landmarks)  #landmarks of x y and z
        #print(mp_hands.HAND_CONNECTIONS) #prints the connections of your landmarks
        

       
       
           

        



cv2.release()
cv2.closeAllWindows()

