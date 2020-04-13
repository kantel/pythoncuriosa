from PIL import Image, ImageFilter
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

im_path = os.path.join("images", "sechseck.jpg")
im = Image.open(im_path)

# Mögliche vordefinierte Filter sind BLUR, CONTOUR, DETAIL, EDGE_ENHANCED,
# EDGE_ENHANCED_MORE, EMBOS, FIND_EDGES, SHARPEN, SMOOTH, SMOOTH_MORE
filter_im = im.filter(ImageFilter.CONTOUR)

filter_im.show()
