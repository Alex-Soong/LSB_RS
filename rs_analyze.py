from cProfile import label
from os import terminal_size
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

import sys


# 计算单个8*8图像块的像素相关度
def calcuRelate(_block, size=8):

    pre = _block[0][0]
    x = 0
    y = 0
    res = 0
    for i in range(1, size*size):
        pre = int(pre)
        res += abs(int(_block[x][y]) - pre)
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


# 生成一个随机8*8的布尔矩阵，用作正负翻转的模式块
def model(ratio=0.5):

    ls = []
    t = int(ratio*64)
    for i in range(t):
        ls.append(True)
    for i in range(64 - t):
        ls.append(False)
    random.shuffle(ls)
    res = np.array(ls).reshape(8, 8)
         
    return res





# 正或负翻转   _ratio为翻转的比例
def turn(matr, model, nonPositive=True):

    m = matr.shape[0]
    n = matr.shape[1]

    res = np.empty((m, n), dtype=int)
    for i in range(m):
        for j in range(n):
            t = int(matr[i][j])
            k = model[i][j]
            if k == True:
                if nonPositive and t > 0 and t < 255:  # 非正翻转
                    res[i][j] = t + 2 * (t % 2) - 1
                elif nonPositive == False:     # 非负翻转
                    res[i][j] = t - 2 * (t % 2) + 1
                else:
                    res[i][j] = t
            else:
                res[i][j] = t
 
    return res


# 计算Rm、R_m、Sm和S_m值
def calcuRmSmR_mS_m(matr, model):

    blocks = matrixCut(matr)
    blockNum = blocks.shape[0]      # 图像块的个数 
    r1 = 0     # Rm
    s1 = 0     # Sm
    r2 = 0     # R_m
    s2 = 0     # S_m
    for i in range(blockNum):
        rela0 = calcuRelate(blocks[i])
        rela1 = calcuRelate(turn(blocks[i], model, nonPositive=True))
        rela2 = calcuRelate(turn(blocks[i], model, nonPositive=False))
        if rela1 > rela0:
            r1 += 1
        elif rela1 < rela0:
            s1 += 1
        if rela2 > rela0:
            r2 += 1
        elif rela2 < rela0:
            s2 += 1
    
    return r1/blockNum, s1/blockNum, r2/blockNum, s2/blockNum


def draw4Lines(x, y1, y2, y3, y4, figureNo):
    plt.figure(figureNo)
    plt.plot(x, y1, label="$R_{m}$")
    plt.plot(x, y2, label="$S_{m}$")
    plt.plot(x, y3, label="$R_{-m}$")
    plt.plot(x, y4, label="$S_{-m}$")
    plt.xlabel("Ratio")
    plt.ylabel("Value")
    plt.legend()
    plt.title("$R_{m}$, $S_{m}$, $R_{-m}$, $S_{-m}$")
    

if __name__ == '__main__':
    
    ratios = [0, 0.1, 0.25, 0.5, 0.75, 1]   # 隐写率
    Rps = []   # 四个列表，分别存放Rm、Sm、R_m、S_m的值
    Sps = []
    Rns = []
    Sns = []
    model = model()
    
    fileName = "123_grey.bmp"
    im0 = Image.open(fileName)
    x0 = np.array(im0)
    Rp, Sp, Rn, Sn = calcuRmSmR_mS_m(x0, model)
    print(Rp, Sp, Rn, Sn)
    Rps.append(Rp)
    Sps.append(Sp)
    Rns.append(Rn)
    Sns.append(Sn)
    for i in range(1, 5 + 1):
        fileName = "123_grey_written"+ str(i) + ".bmp"
        im1 = Image.open(fileName)
        x1 = np.array(im1)
        Rp, Sp, Rn, Sn = calcuRmSmR_mS_m(x1, model)
        print(Rp, Sp, Rn, Sn)
        Rps.append(Rp)
        Sps.append(Sp)
        Rns.append(Rn)
        Sns.append(Sn)
    
    plt.close('all')
    draw4Lines(ratios, Rps, Sps, Rns, Sns, 1)
    plt.show()
    
    print(model)
    
    # if len(sys.argv) > 2:
    #     inputFileName0 = sys.argv[1]
    #     inputFileName1 = sys.argv[2]
    # b = np.arange(256).reshape(16, 16)
    # shape = (2, 2, 8, 8)
    
    # strides = b.itemsize * np.array([128, 8, 16, 1])
    # b = np.lib.stride_tricks.as_strided(b, shape=shape, strides=strides) 
    # b = b.reshape(4, 8, 8)
    # b = matrixCut(b)
    # print(b)
    # print(calcuRelate(b[0]))
    