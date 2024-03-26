import qrcode
data="https://call.whatsapp.com/video/Tw2WSNeAo9c769h1on5yhD"
qr=qrcode.QRCode(version=1,box_size=10,border=5)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color='blue',back_color='white')
img.save('whatsapp.png')