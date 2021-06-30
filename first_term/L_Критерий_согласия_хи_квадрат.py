import numpy as np
from scipy import stats

fr = open('input.txt', 'r')

n = int(fr.readline())


a = list(map(float, fr.readline().split()))
a = np.array(a)

b = list(map(float, fr.readline().split()))
b = np.array(b)
b *= np.sum(a)

c, p = stats.chisquare(a, b)

open('output.txt', 'w').write(str(p))


