# ImageCaptcha

from captcha.image import ImageCaptcha

# define dimension of ur captcha image
img = ImageCaptcha(width= 200, height=80)

gen_captcha = img.generate('uS56ha')

img.write('xSS56ha','./captcha1.jpg')