#pip install pillow
from PIL import Image

f = "C:/users/user/folder"
im = Image.open(f + '/image_file.png')
width, height = im.size
print(str(width) + ' x ' + str(height))
