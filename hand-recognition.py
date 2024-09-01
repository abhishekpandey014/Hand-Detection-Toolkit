import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.5, maxHands=1)

while True:
    success, img = cap.read()

    hands, img = detector.findHands(img)  

    if hands:
        hand = hands[0]  # Get the first detected hand
        lmList = hand['lmList']  # List of landmarks
        bbox = hand['bbox']  # Bounding box of the hand

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

