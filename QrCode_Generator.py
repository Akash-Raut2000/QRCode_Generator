import pyqrcode
import png
from pyqrcode import QRCode

# String which represents the QR code
s = "https://github.com/Akash-Raut2000"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
#url.svg("myqr.svg", scale=8)

# Create and save the png file naming "myqr.png"
url.png('Akash_Github_link.png', scale=6)