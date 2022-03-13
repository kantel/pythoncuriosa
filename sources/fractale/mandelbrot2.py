from PIL import Image
import os

maxlimit = 2.0
size = 600
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

# Parameter
left   = -2.25
right  = 0.75
bottom = -1.5
top    = 1.5
maxiter = 20

def mandelbrot():
    img = Image.new("RGB", (size, size), (0, 0, 0))
    for x in range(size):
        cr = left + x*(right - left)/size
        for y in range(size):
            ci = bottom + y*(top - bottom)/size
            c = complex(cr, ci)
            z = 0.0
            i = 0
            for i in range(maxiter):
                if abs(z) > maxlimit:
                    break
                z = (z**2) + c
                if i == (maxiter - 1):
                    color = (0, 0, 0)
                else:
                    # color = (i%17*16, i%9*32, i%5*64)
                    color = (i%5*64, i%17*16, i%9*32)
                img.putpixel((x, y), color)
    return img


mandel = mandelbrot()

mandel.save("images/mandel1.png")
# mandel.show()

print("I did it, Babe!")

