import numpy as np

fr = open('input.txt', 'r')

n = int(fr.readline())

x = list(map(float, fr.readline().split()))
y = list(map(float, fr.readline().split()))

numerator = np.sum((x - np.mean(x)) * (y - np.mean(y)))
denominator = np.sum((x - np.mean(x))**2)

if denominator == 0 or numerator == 0:
    open('output.txt', 'w').write(str(0) + ' ' + str(0))
    exit(0)

a = numerator / denominator
b = np.mean(y) - a * np.mean(x)

open('output.txt', 'w').write(str(a) + ' ' + str(b))
