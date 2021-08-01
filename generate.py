import random, string, sys

import pyqrcode

def random_filename(n):
  r_l = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
  return "".join(r_l)

def generate_qrcode(url: str, version=3):
  c = pyqrcode.create(url, error="L", version=version, mode="binary")
  return c

def generate_qrcode_image(url: str):
  filename = f"{random_filename(6)}.png"
  generate_qrcode(url).png(f"./output/{filename}", scale=5, module_color=[0,0,0,128], background=[255,255,255])
  return filename

if __name__ == "__main__":
  if len(sys.argv) >= 2:
    try:
      filename = generate_qrcode_image(sys.argv[1])
      print(f"QRコード, {filename}が正しく生成されました.")
    except Exception as e:
      print("Error: QRコードが正しく生成されませんでした.", file=sys.stderr)
  else:
    print("Error: 第2引数にURLを指定してください.", file=sys.stderr)