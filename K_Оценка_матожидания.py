import numpy as np
from scipy import stats

fr = open('input.txt', 'r')
n, confidence, o = map(float, fr.readline().split())
x = np.array(list(map(float, fr.readline().split())))
m = np.mean(x)
if o > 0:
    t = stats.norm.ppf(confidence / 2 + 0.5)
    u = t * (o / n)**.5
else:
    t = stats.t.isf((1 - confidence) / 2, n - 1)
    s = np.sum((x - m)**2) / (n - 1)
    u = t * ((s / (n - 1))**.5)
print(m - u, m + u, file=open('output.txt', 'w'))
