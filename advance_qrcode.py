import qrcode
from PIL import Image


qr=qrcode.QRCode(version =1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data("https://github.com/sachinkumar202/Python_Course")
qr.make(fit=True)
img=qr.make_image(fill_color='black',back_color="cyan")
img.save("Python_Course_repo.png")