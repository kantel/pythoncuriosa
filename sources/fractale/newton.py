# Newton fractals
from PIL import Image
import os

imgx = 512
imgy = 512
image = Image.new("RGB", (imgx, imgy))

file_path = os.path.dirname(os.path.abspath(__file__))
image_folder = os.path.join(file_path, "images")

# drawing area
xa = -1.0
xb = 1.0
ya = -1.0
yb = 1.0

maxIt = 20 # max iterations allowed
h = 1e-6 # step size for numerical derivative
eps = 1e-3 # max error allowed

# put any complex function here to generate a fractal for it!
def f(z):
    return z * z * z - 1.0

# draw the fractal
for y in range(imgy):
    zy = y * (yb - ya) / (imgy - 1) + ya
    for x in range(imgx):
        zx = x * (xb - xa) / (imgx - 1) + xa
        z = complex(zx, zy)
        for i in range(maxIt):
            # complex numerical derivative
            dz = (f(z + complex(h, h)) - f(z)) / complex(h, h)
            z0 = z - f(z) / dz # Newton iteration
            if abs(z0 - z) < eps: # stop when close enough to any root
                break
            z = z0
        # image.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16))
        # image.putpixel((x, y), (i % 5 * 64, i % 9 * 32, i % 17 * 16))
        image.putpixel((x, y), (i % 5 * 64, i % 17 * 16, i % 9 * 32))

image.show()
image.save(os.path.join(image_folder, "newtonFractal2.png"), "PNG")