
import pyqrcode

from pyqrcode import QRCode

url = pyqrcode.create ('https://www.linkedin.com/in/robson-müller-672a0a31/')
url.svg ('uca-url.svg', scale = 4)
url.eps ('uca-url.eps', scale = 2)
print (url.terminal (quiet_zone = 1))


