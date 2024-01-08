from generativepy.drawing import make_image, setup
from generativepy.color import Color
from generativepy.geometry import Rectangle
import os

file_path = os.path.dirname(os.path.abspath(__file__))
image_folder = os.path.join(file_path, "images")

def draw(ctx, pixel_width, pixel_height, frame_no, frame_count):

    setup(ctx, pixel_width, pixel_height, background=Color(0.92))

    color0 = Color(0.18, 0.20, 0.22)
    Rectangle(ctx).of_corner_size((50, 150), 300, 50).fill(color0)
    color1 = Color(0.77, 0.47, 0.22, 0.7)
    Rectangle(ctx).of_corner_size((100, 50), 50, 200).fill(color1)
    color2 = Color(0.45, 0.69, 0.91, 0.7)
    Rectangle(ctx).of_corner_size((170, 70), 50, 200).fill(color2)
    color3 = Color(0.94, 0.29, 0.17, 0.7)
    Rectangle(ctx).of_corner_size((240, 90), 50, 200).fill(color3)

make_image(os.path.join(image_folder, "rectangle.png"), draw, 500, 400)
print("I did it, Babe!")