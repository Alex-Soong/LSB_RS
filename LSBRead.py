from PIL import Image
import numpy as np
import bitstring as bs
import sys, os

fileName = "2333_grey_written.bmp"

im0 = Image.open(fileName)
x = np.array(im0)

fSize = x.ravel().shape[0]

for i in range(fSize):
    t = x.ravel()[i] % 2
    print(t, end="")