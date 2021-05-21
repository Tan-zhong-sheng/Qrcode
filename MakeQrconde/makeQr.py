from PIL import Image
import qrcode
#带图片的编码方式
from PIL import Image
qr = qrcode.QRCode(
    version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
qr.add_data('http://www.baidu.com')
qr.make(fit=True)#fit=True如过你没有传入大小的话，自动给你一个合适的大小
img = qr.make_image()
img = img.convert("RGBA")
icon = Image.open("dog.jpg")
img_w, img_h = img.size
factor = 4
size_w = int(img_w / factor)
size_h = int(img_h / factor)
icon_w, icon_h = icon.size
if icon_w > size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h
icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
w = int((img_w - icon_w) / 2)
h = int((img_h - icon_h) / 2)
icon = icon.convert("RGBA")
img.paste(icon, (w, h), icon)
img.show()
img.save('test.png')

