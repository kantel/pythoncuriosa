import rembg
import numpy as np
from PIL import Image
import os

DATAPATH = os.path.join(os.getcwd(), "images")

input_path = os.path.join(DATAPATH, "zuschauer08.png")
output_path = os.path.join(DATAPATH, "zuschauer08_bgrem.png")

# Load the input image
input_image = Image.open(input_path)

# Convert the input image to a numpy array
input_array = np.array(input_image)

# Apply background removal using rembg
output_array = rembg.remove(input_array)

# Create a PIL Image from the output array
output_image = Image.fromarray(output_array)

# Save the output image
output_image.save(output_path)
result = Image.new('RGBA', (input_image.width * 2, input_image.height))
result.paste(input_image, (0, 0))
result.paste(output_image, (input_image.width, 0))
result.show()

print("I did it, Babe!")