import cv2
import mediapipe as mp
import time

# python HandTrackingMin.py

cap = cv2.VideoCapture(0)                                  # 0 = webcam, 1 = ext camera

mpHands = mp.solutions.hands
hands = mpHands.Hands()                               #LA  #functions; hands = 2, etc
mpDraw = mp.solutions.drawing_utils                         

cTime = 0
pTime = 0

while True:
    success, img = cap.read()                                # reads img
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)             # img to rgb ?= LA only understands rgb
    results = hands.process(imgRGB)                          # Processing img
    # print(results.multi_hand_landmarks)                      # detects hands, print landmarks
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:         # for each hand
            for id, lm in enumerate(handLms.landmark):
                print(id,lm)

                h, w, c = img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)

                if id==8:
                    cv2.circle(img, (cx,cy), 20, (255,0,255), cv2.FILLED)
           
           
            # mpDraw.draw_landmarks(img, handLms)               # shows pos (red dot) while tracking
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)               # shows pos (red dot) while tracking WITH  CONNECTING WITH GREEEN LINE


    cTime = time.time()                                     #calc fps
    fps   = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0, 255), 3)    # source, value, pos, font, scale, colour, Thckness

    cv2.imshow("image",img)                                  # shows image                
    cv2.waitKey(1)                                           # 1ms delay

