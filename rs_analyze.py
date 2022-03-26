import numpy as np

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


b = np.arange(64).reshape(8, 8)
print(b)
print(calcuRelate(b))