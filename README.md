运行环境：Windows

主要功能：实现LSB隐写，并对隐写后的图片进行RS分析

语言：Python

主要用到的库：NumPy、PIL、bitstring



color2grey.py：将彩色的bmp图像转为灰度图

命令：py .\color2grey.py [filename]



LSBWrite.py：将二进制信息以LSB方式写入bmp图像

命令：py .\LSBWrite.py [file1] [file2]     // 将file2以二进制形式，LSB隐写至file1



