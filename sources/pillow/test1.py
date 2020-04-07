from PIL import Image
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)
im_path = os.path.join("images", "sechseck.jpg")

im = Image.open(im_path)

im.show()
