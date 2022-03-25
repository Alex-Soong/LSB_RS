from PIL import Image
import numpy as np
import sys, os


def LSBReplace(_value, _bit):
    lsb = _value % 2
    _value = _value - lsb + _bit
    return _value


def write(fileName, infotoWrite=""):
    im0 = Image.open(fileName)
    x = np.array(im0)

    length = x.ravel().shape[0]
    for i in range(length):
        x.ravel()[i] = LSBReplace(x.ravel()[i], 0)

    im1 = Image.fromarray(x)
    im1.save(fileName[:-4] + "_written.bmp")


if __name__ == '__main__':

    # if len(sys.argv) > 2:
    inputName = sys.argv[1]
    #     inputName0 = sys.argv[2]
    # else:
    #     print("未指定文件名")
    #     os._exit(0)

    write(inputName)


