import cv2
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(0) # Change if value to 1 if your using webcam.

cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)

startDist = None
scale = 0
cx, cy = 500, 500

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    #importing image
    img1 = cv2.imread('image/relax.jpeg')

    #cv2.imshow("Image 1",img1)
    #gesture
    if len(hands) == 2:

        #print(detector.fingersUp(hands[0]), detector.fingersUp(hands[1])) #shows values for both right and left hands
        if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:
            #print("Zoom Gesture")
            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]

            #point 8 is the tip of the index finger
            if startDist is None:
                #lmList1[8],lmList2[8]
                #length, info, img = detector.findDistance(lmList1[8],lmList2[8],img)
                length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)

                startDist = length

            #length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)

            length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
            scale = int((length - startDist)//2)
            cx, cy = info[4:]
            print(scale)
    else:
        startDist = None
    try:
        h1, w1, _ = img1.shape
        newH, newW = ((h1+scale)//2)*2, ((w1+scale)//2)*2
        img1 = cv2.resize(img1, (newW, newH))

        img[cy-newH//2:cy+newH//2, cx-newW//2:cx+newW//2] = img1
    except:
        pass
    cv2.imshow("Image", img)
    cv2.waitKey(1)
