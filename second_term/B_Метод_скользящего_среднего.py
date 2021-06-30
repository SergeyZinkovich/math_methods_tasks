import numpy as np


def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w


f = open('input.txt', 'r')
n, m = map(int, f.readline().split())
data = list(map(float, f.readline().split()))

print(*moving_average(data, m), file=open('output.txt', 'w'))
