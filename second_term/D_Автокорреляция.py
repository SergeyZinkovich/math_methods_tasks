import numpy as np

f = open('input.txt', 'r')
n, m = map(int, f.readline().split())
data = list(map(float, f.readline().split()))

ans = []
for l in range(1, m+1):
    ans.append(np.corrcoef(data[:n-l], data[l:])[0, 1])

print(*ans, file=open('output.txt', 'w'))