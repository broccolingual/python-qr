import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
qrd = cv2.QRCodeDetector()

while cap.isOpened():
  ret, frame = cap.read()
  if ret:
    retval, decoded_info, points, straight_qrcode = qrd.detectAndDecodeMulti(frame)
    if retval:
      print(decoded_info)