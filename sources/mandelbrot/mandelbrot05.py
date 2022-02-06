from mandelbrot import MandelbrotSet
from PIL import Image

mandelbrot_set = MandelbrotSet(max_iterations=20)

width, height = 512, 512
scale = 0.0075
BLACK_AND_WHITE = "1"

image = Image.new(mode=BLACK_AND_WHITE, size=(width, height))
for y in range(height):
    for x in range(width):
        c = scale * complex(x - width / 1.5, height / 2 - y)
        image.putpixel((x, y), c not in mandelbrot_set)
image.show()