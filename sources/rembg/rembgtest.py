from rembg import remove
from PIL import Image
import os

DATAPATH = os.path.join(os.getcwd(), "images")

input_path = os.path.join(DATAPATH, "me2022.jpg")
output_path = os.path.join(DATAPATH, "output.png")

input = Image.open(input_path)
output = remove(input)

output.save(output_path)