from PIL import Image
import numpy as np
import bitstring as bs
import sys, os

# fileName = "2333_grey_written.bmp"
def LSBRead(fileName="2333_grey_written.bmp", bitNum=0):

    ret = ""        
    im0 = Image.open(fileName)
    x = np.array(im0)

    if bitNum == 0:
        fSize = x.ravel().shape[0]
    else:
        fSize = bitNum

    for i in range(fSize):
        t = x.ravel()[i] % 2
        ret = ret + str(t)

    return ret


if __name__ == '__main__':
    print(LSBRead())
