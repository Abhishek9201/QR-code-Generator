import qrcode  # type: ignore
from PIL import Image  # type: ignore

qr = qrcode.QRCode(version=1,error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 10, border = 4,)

qr.add_data("https://www.linkedin.com/in/abhishek-singh-54028820a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")

qr.make(fit = True)
img = qr.make_image(fill_color = "red",back_color = "white")

img.save("advanceqr_linkedin.png")
