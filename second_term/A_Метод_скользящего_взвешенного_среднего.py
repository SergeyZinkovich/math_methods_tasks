import numpy as np

f = open('input.txt', 'r')
n, m = map(int, f.readline().split())
w = np.array(list(map(float, f.readline().split())))
data = list(map(float, f.readline().split()))

x = []
for i in range(n - m + 1):
    x.append(data[i:i+m])

x = np.array(x)
ans = np.ma.average(x, weights=w, axis=1)

print(*ans, file=open('output.txt', 'w'))
