import numpy as np
import math
a = list(map(float, open('input.txt', 'r').read().split()[1:]))
k = 1 + math.floor(np.log2(len(a)))

_max = max(a)
_min = min(a)
h = (_max - _min) / k

f = open('output.txt', 'w')

if h == 0:
    exit()

for i in range(k):
    if i == k - 1:
        a1 = list(filter(lambda x: _min + i * h <= x, a))
    else:
        a1 = list(filter(lambda x: _min + i * h <= x < _min + (i + 1) * h, a))
    f.write(str(len(a1)) + ' ')
