# 利用方法

## QR コード生成

`pipenv run g <URL>`
<br>とすることで QR コードの画像を出力することができます。
<br>生成された画像は`./output`に png 画像として出力されます。

## QR コード読み取り(画像から)

`pipenv run r <filepath>`
<br>とすることで QR コードの画像から URL を抽出することができます。

## QR コード読み取り(Web カメラから)

`pipenv run d <filepath>`
<br>とすることで Web カメラ等のデバイスから QR コード を読み取ることができます。
