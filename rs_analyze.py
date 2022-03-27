import random
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


# 正或负翻转   _ratio为翻转的比例
def turn(matr, nonPositive=True, _ratio=0.5):

    m = matr.shape[0]
    n = matr.shape[1]
    
    res = np.empty((m, n), dtype=int)
    for i in range(m):
        for j in range(n):
            t = matr[i][j]
            k = random.random()  # 随机生成[0, 1)区间的浮点数
            if k < _ratio:
                if nonPositive:
                    res[i][j] = t + 2 * (t % 2) - 1
                else:
                    res[i][j] = t - 2 * (t % 2) + 1

    return res


# 计算Rm、R_m、Sm和S_m值
def calcuRmSmR_mS_m(matr):

    blocks = matrixCut(matr)
    blockNum = blocks.shape[0]      # 图像块的个数 
    r1 = 0
    r2 = 0
    s1 = 0
    s2 = 0
    for i in range(blockNum):
        rela0 = calcuRelate(blocks[i])
        rela1 = calcuRelate(turn(blocks[i], nonPositive=True))
        rela2 = calcuRelate(turn(blocks[i], nonPositive=False))
        if rela1 > rela0:
            r1 += 1
        elif rela1 < rela0:
            s1 += 1
        if rela2 > rela0:
            r2 += 1
        elif rela2 < rela0:
            s2 += 1
    
    return r1/blockNum, r2/blockNum, s1/blockNum, s2/blockNum


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
    