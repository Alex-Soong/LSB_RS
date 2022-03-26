from PIL import Image
import numpy as np
import bitstring as bs
import sys, os

# fileName = "2333_grey_written.bmp"
def LSBRead(fileName="2333_grey_written.bmp", readLength=-1):

    ret = ""        
    im0 = Image.open(fileName)
    x = np.array(im0)

    fSize = x.ravel().shape[0]
    
    if readLength == -1:
        length = fSize
    else:
        length = readLength if readLength < fSize else fSize

    for i in range(length):
        t = x.ravel()[i] % 2
        ret = ret + str(t)

    return ret


if __name__ == '__main__':
    print(LSBRead())
