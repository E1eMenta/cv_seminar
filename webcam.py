import cv2
import numpy as np

cap = cv2.VideoCapture(0)

counter = 0
while (True):
    ret, frame = cap.read()

    if counter % 10 == 0:
        cv2.imwrite(f"frame_{counter}.png", frame)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    counter += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
