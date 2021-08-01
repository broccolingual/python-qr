import sys

import cv2
import numpy as np

def read_qrcode(filepath: str):
  img_bgr = cv2.imread(filepath, cv2.IMREAD_COLOR)
  qrd = cv2.QRCodeDetector()
  retval, decoded_info, points, straight_qrcode = qrd.detectAndDecodeMulti(img_bgr)
  if retval:
    return decoded_info

if __name__ == "__main__":
  if len(sys.argv) >= 2:
    try:
      url = read_qrcode(sys.argv[1])
      print(url)
      print(f"QRコードが正しく読み込まれました.")
    except Exception as e:
      print("Error: QRコードが正しく読み込まれませんでした.", file=sys.stderr)
  else:
    print("Error: 第2引数に画像パスを指定してください.", file=sys.stderr)