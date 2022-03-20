from PIL import Image
import numpy as np

im = Image.open("123.bmp")
x = np.array(im)

for xi in x:
    print(xi)