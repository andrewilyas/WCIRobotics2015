import cv2
from heuristics import Heuristics
from camerahelper import CameraHelper

cap = cv2.VideoCapture(0)
thresh = 60
i = 0
ch = CameraHelper(0, 0, 0, 0, 0, 0)
while True:
    i += 1
    thresh += 10
    print thresh
    ret, frame = cap.read()
    frame = ch.resizeImage(frame, 4, 4)
    h = Heuristics(frame, thresh=thresh)
    cv2.imshow('frame', h.lineIMG)
    lineAngles = h.lineAngles()
    print len(h.lines)*(lineAngles['LeftStd'] + lineAngles['RightStd'])
    if len(h.lines)*(lineAngles['LeftStd'] + lineAngles['RightStd']) < 5 and len(h.lines) < 50 and (lineAngles['Left'] > 45 or lineAngles['Right'] > 45):
        print len(h.lines)
        print lineAngles
        break
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
