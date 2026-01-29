import qrcode

data = input("Enter website URL: ").strip()
filename = input("Enter file name: ").strip()  # .strip = remove white spaces.

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)

print(f"QR Code generated, file saved as : {filename}")
