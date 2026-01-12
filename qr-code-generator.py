import qrcode

url = input("Enter the URL or text to encode in the QR code: ")
file = input("Enter the filename to save the QR code (e.g., qrcode.png): ")
file_path = f"/{file}"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print(f"✅ QR code saved to {file_path}")

