from PIL import Image
import numpy as np
import sys, os

if len(sys.argv) > 1:
    fileName = sys.argv[1]
else:
    print("未指定文件名")
    os._exit(0)

im0 = Image.open(fileName)
x = np.array(im0)

im1 = Image.fromarray(x)
im1.save(fileName[:-4] + "_written.bmp")