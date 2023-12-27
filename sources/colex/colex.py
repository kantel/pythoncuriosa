import numpy as np 
import os
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 
from PIL import Image

N_COLORS = 10    # Number of Colors

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)
im_path = os.path.join("images", "downtown02.jpg")
im = Image.open(im_path)
im.show()
image = mpimg.imread(im_path)
w, h, d = tuple(image.shape)
# print(w, h, d)
pixels = np.reshape(image, (w*h, d))
print("vor model")
from sklearn.cluster import KMeans
model = KMeans(n_clusters = N_COLORS, random_state = 42).fit(pixels)
print("vor palette")
palette = np.uint8(model.cluster_centers_)

plt.imshow([palette])
plt.show()

print("I did it, Babe!")