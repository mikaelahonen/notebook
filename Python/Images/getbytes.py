import os
import base64

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
f = os.path.join(__location__, 'getbytes.png')
with open(f, 'rb') as source_image:
    source_bytes = base64.b64encode(source_image.read())
    print(source_bytes)
