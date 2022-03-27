from LSBRead import LSBRead

for i in range(1, 5 + 1):
    bits = LSBRead("123_grey_written" + str(i) + ".bmp")
    zeros = 0
    ones = 0
    for c in bits:
        if c == '0':
            zeros += 1
        else:
            ones += 1
    
    print(zeros, ones)