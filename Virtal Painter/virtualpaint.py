import cv2 
import numpy as np
import time
import os
import HandTrackingModule as htm

# venv\scripts\activate
# python virtualpaint.py

#1 Import Image
#2 Find Hand Landmarks
#3 Check up finger
#4 Selection Mode: Two finger up
#5 Drawing mode  : One finger up


folderPath = "Mini Project UI"
myList = os.listdir(folderPath)
# print(myList)

overlayList = []
for impath in myList:
    image = cv2.imread(f'{folderPath}/{impath}')
    overlayList.append(image)
# print(len(overlayList))

header = overlayList[0]
drawcolor = (255,0,0)
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

img1 = cv2.imread("Mini Project UI/1.jpg")
# print("Image shape:", img1.shape)  # (height, width, channels)

detector = htm.HandDetector(detectcon=0.85)

while True:
    #1 Import Image
    success,img = cap.read()            
    img = cv2.flip(img,1)

    #2 Find Hand Landmarks
    img = detector.findHands(img)
    lmList = detector.FindPosition(img, draw=False)

    if len(lmList) !=0:
        # print(lmList)
        # tip of index finger
        x1, y1 = lmList[8][1:]
        # tip of middle finger
        x2, y2 = lmList[12][1:]

        #3 Check up finger
        fingers = detector.fingersUP()
        print(fingers)

        #4 Selection Mode: Two finger up
        if fingers[1] and fingers[2]:
            print("Selection Mode")
            # cv2.rectangle(img, (x1,y1 - 25), (x2, y2 + 25), (255, 0, 255), cv2.FILLED)

            if y1 < 200:
                if 225 < x1 < 415:
                   header = overlayList[0]
                   drawcolor = (0,0,255)
                elif 510< x1 < 680:
                    header = overlayList[1]
                    drawcolor = (255,0,0)
                elif 830 < x1 < 1020:
                    header = overlayList[2]
                    drawcolor = (128,0,128)
                elif 1110 < x1 < 1230:
                    header = overlayList[3]
                    drawcolor = (0,0,0)
                cv2.rectangle(img, (x1,y1 - 25), (x2, y2 + 25), drawcolor, cv2.FILLED)

        #5 Drawing mode  : One finger up
        if fingers[1] and fingers[2]==False:
            print("Drawing Mode")
            cv2.circle(img, (x1,y1), 25, drawcolor, cv2.FILLED)


    #Setting header imgae
    img[0:100, 0:1280] = header
    cv2.imshow("Image",img)
    cv2.waitKey(1)