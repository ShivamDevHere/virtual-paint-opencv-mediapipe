import cv2
import mediapipe as mp
import time

# python HandTrackingMin.py
# cap = cv2.VideoCapture(0)                                  # 0 = webcam, 1 = ext camera

class HandDetector():
    def __init__(self, mode=False, maxHands=2, detectcon=0.5, trackcon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectcon = detectcon
        self.trackcon = trackcon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, max_num_hands=self.maxHands, min_detection_confidence=self.detectcon, min_tracking_confidence=self.trackcon)                               #LA  #functions; hands = 2, etc
        self.mpDraw = mp.solutions.drawing_utils   

        self.tipIds = [4,8,12,16,20] 

    def findHands(self, img, draw = True):                     
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)             # img to rgb ?= LA only understands rgb
        self.results = self.hands.process(imgRGB)                          # Processing img
        # print(results.multi_hand_landmarks)                      # detects hands, print landmarks
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:         # for each hand
                if draw:
                    # mpDraw.draw_landmarks(img, handLms)               # shows pos (red dot) while tracking
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)               # shows pos (red dot) while tracking WITH  CONNECTING WITH GREEEN LINE
        return img

    def FindPosition(self, img, handNo = 0, draw = True):
        self.lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                self.lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx,cy), 20, (255,0,255), cv2.FILLED)
        return self.lmList
           
    def fingersUP(self):
        fingers = []
        # if len(self.lmList) == 0:
        #     return []
        
        #Thumb
        if self.lmList[self.tipIds [0]][1] < self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        #4 Fingers
        for id in range(1,5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers
                

def main():
    cTime = 0
    pTime = 0
    cap = cv2.VideoCapture(0)                                  # 0 = webcam, 1 = ext camera
    detector = HandDetector()

    while True:
        success, img = cap.read()   
        img = detector.findHands(img) 
        lmList = detector.FindPosition(img,draw = False)
        # img = detector.findHands(img,draw = False)            #To stop drawing
        # lmList = detector.FindPosition(img, draw = False)     #To stop custom circle
        if len(lmList) !=0:
            print(lmList[4])

        cTime = time.time()                                     #calc fps
        fps   = 1/(cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0, 255), 3)    # source, value, pos, font, scale, colour, Thckness

        cv2.imshow("image",img)                                  # shows image                
        cv2.waitKey(1)                                           # 1ms delay

if __name__ == "__main__":
    main()