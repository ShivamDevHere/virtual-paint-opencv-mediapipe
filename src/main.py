import cv2 
import numpy as np
import time
import os
import src.HandTrackingModule as htm

"""
Ths file is divided into 5 parts
1. Import Image
2. Find Hand Landmarks
3. Check up finger
4. Selection Mode: Two finger up
5. Drawing mode  : One finger up
"""

brushThickness = 15
eraserThickness = 135

xp,yp = 0,0

folderPath = "assets/ui"

myList = [
    "red_selected.jpg",
    "blue_selected.jpg",
    "purple_selected.jpg",
    "eraser_selected.jpg",
]

overlayList = []
for imgName in myList:
    image = cv2.imread(os.path.join(folderPath, imgName))
    overlayList.append(image)

header = overlayList[0]

drawcolor = (255,0,0)
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

# img1 = cv2.imread("assets/ui/red_selected.jpg")
# print("Image shape:", img1.shape)  # (height, width, channels)

detector = htm.HandDetector(detectcon=0.85)

imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while True:

    #1 Import Image
    success,img = cap.read()            
    img = cv2.flip(img,1)

    #2 Find Hand Landmarks
    img = detector.findHands(img)
    lmList = detector.FindPosition(img, draw=False)

    if len(lmList) !=0:
        # tip of index finger
        x1, y1 = lmList[8][1:]
        # tip of middle finger
        x2, y2 = lmList[12][1:]

        #3 Check up finger
        fingers = detector.fingersUP()
        print(fingers)

        #4 Selection Mode: Two finger up
        if fingers[1] and fingers[2]:
            # cv2.rectangle(img, (x1,y1 - 25), (x2, y2 + 25), (255, 0, 255), cv2.FILLED)
            xp,yp= 0,0

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
            cv2.circle(img, (x1,y1), 25, drawcolor, cv2.FILLED)
            
            if( xp == 0 and yp == 0):
                xp,yp = x1,y1

            if drawcolor == (0,0,0):
                cv2.line(img, (xp,yp), (x1,y1), drawcolor, eraserThickness)
                cv2.line(imgCanvas, (xp,yp), (x1,y1), drawcolor, eraserThickness)
            else:
                cv2.line(img, (xp,yp), (x1,y1), drawcolor, brushThickness)
                cv2.line(imgCanvas, (xp,yp), (x1,y1), drawcolor, brushThickness)

            xp,yp = x1,y1

        imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
        _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
        imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
        img = cv2.bitwise_and(img, imgInv)
        img = cv2.bitwise_or(img, imgCanvas)

    #Setting header imgae
    img[0:100, 0:1280] = header
    img = cv2.addWeighted(img,0.5,imgCanvas,0.5,0)
    cv2.imshow("Image",img)
    cv2.imshow("Canvas",imgCanvas)
    cv2.waitKey(1)