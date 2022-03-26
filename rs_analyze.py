import numpy as np
import sys

# 计算单个8*8图像块的像素相关度
def calcuRelate(_block):
    size = 8
    pre = _block[0][0]
    x = 0
    y = 0
    res = 0
    for i in range(size*size):
        res += abs(_block[x][y] - pre)
        pre = _block[x][y]
        if (x == 0 or x == 7) and y % 2 == 0:
            y += 1
        elif (y == 0 or y == 7) and x % 2 == 1:
            x += 1
        elif (x + y) % 2 == 1:
            x += 1
            y -= 1
        else:
            x -= 1
            y += 1
    return res


# 将矩阵分割为若干小块(默认8*8) 
def matrixCut(A, edgeLen=8):
    m = A.shape[0] // edgeLen
    n = A.shape[1] // edgeLen
    res = A[:edgeLen * m][:edgeLen * n]
    shape = (m, n, edgeLen, edgeLen)
    strides = res.itemsize * np.array([n * edgeLen ** 2, edgeLen, n * edgeLen, 1])
    res = np.lib.stride_tricks.as_strided(res, shape=shape, strides=strides)
    res = res.reshape(m * n, edgeLen, edgeLen)
    return res 


if __name__ == '__main__':
    
    # if len(sys.argv) > 2:
    #     inputFileName0 = sys.argv[1]
    #     inputFileName1 = sys.argv[2]
    b = np.arange(256).reshape(16, 16)
    # shape = (2, 2, 8, 8)
    
    # strides = b.itemsize * np.array([128, 8, 16, 1])
    # b = np.lib.stride_tricks.as_strided(b, shape=shape, strides=strides) 
    # b = b.reshape(4, 8, 8)
    b = matrixCut(b)
    print(b)
    print(calcuRelate(b[0]))
    