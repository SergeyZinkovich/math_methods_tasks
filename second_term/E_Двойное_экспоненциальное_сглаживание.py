import numpy as np

file = open('input.txt', 'r')
n, a, f = map(float, file.readline().split())
data = list(map(float, file.readline().split()))

s = [data[0]]
b = data[1] - data[0]
for l in range(1, len(data)):
    s.append(a*data[l] + (1 - a) * (s[-1] + b))
    b = f * (s[-1] - s[-2]) + (1 - f) * b

print(*s, file=open('output.txt', 'w'))