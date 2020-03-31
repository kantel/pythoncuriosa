import numpy as np
import os
from PIL import Image

# Parameter
in_file = "farbakt.jpg"
out_file = "out.txt"
scale = 0.45
cols = 80
more_levels = False

file_path = os.path.dirname(os.path.abspath(__file__))
image_folder = os.path.join(file_path, "images")

# Graustufenskalen aus: Paul Bourke: Character representation of grey scale images
# http://paulbourke.net/dataformats/asciiart/

# 70 Shades of Gray:
gscale1 = "$@B%8&WM#*oahkbdpqZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'´. "

# 10 Shades of Gray
gscale2 = "@%#*+=-:. "

def get_average(image):
    im = np.array(image)
    w, h = im.shape
    return(np.average(im.reshape(w*h)))

def convert_image_to_ascii(file_name, cols, scale, more_levels):
    # Bilddatei öffnen und zu Graustufen konvertieren
    image_path = os.path.join(image_folder, file_name)
    image = Image.open(image_path).convert("L")
    W, H = image.size[0], image.size[1]
    w = W/cols
    h = w/scale
    rows = int(H/h)
    ascii_img = []
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j + 1)*h)
        # Sonderbehandlung für das letzte Reihe
        if j == rows - 1:
            y2 = H
        ascii_img.append("")
        for i in range(cols):
            x1 = int(i*w)
            x2 = int((i + 1)*w)
            # Sonderbehandlung für die letzte Spalte
            if i == cols - 1:
                x2 = W
            img = image.crop((x1, y1, x2, y2))
            avg = int(get_average(img))
            if more_levels:
                gsval = gscale1[int((avg*69)/255)]
            else:
                gsval = gscale2[int((avg*9)/255)]
            ascii_img[j] += gsval
    return(ascii_img)
    
aimg = convert_image_to_ascii(in_file, cols, scale, more_levels)
f = open(out_file, "w")
for row in aimg:
    f.write(row + "\n")
f.close()
print("I did it, Babe!")