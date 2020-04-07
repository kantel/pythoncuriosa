from PIL import Image, ImageEnhance
import os

R, G, B = 0, 1, 2

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

im_path = os.path.join("images", "sechseck.jpg")
im = Image.open(im_path)

source = im.split()
red = source[R]
green = source[G].point(lambda i: i*0.0)
blue = source[B].point(lambda i: i*0.0)
new_source = [red, green, blue]

new_im = Image.merge(im.mode, new_source)

new_im.show()
