import numpy as np

fr = open('input.txt', 'r')
n = int(fr.readline())
a = np.array([np.array(list(map(float, fr.readline().split()))) for _ in range(n)])
b = np.array(list(map(lambda x: [float(x)], fr.readline().split())))

arr = np.append(a, b, axis=1)

if np.linalg.matrix_rank(a) != n:
    open('output.txt', 'w').write('-1')
    exit(0)

lines = n
columns = n+1

for k in range(1, lines):
    for i in range(k, lines):
        divisor = arr[i][k-1] / arr[k-1][k-1]
        arr[i] -= arr[k-1] * divisor

answer = [arr[lines - 1][columns - 1]/arr[lines - 1][columns - 2]]
shift = columns - 2
lshift = columns - 3
f = 0

for k in range(lines - 2, -1, -1):
    f = arr[k][columns - 1]
    for j in range(shift, lshift, -1):
        f = (f - arr[k][j] * answer[shift - j])
    f /= arr[k][k]
    answer.append(f)
    lshift -= 1
print(*answer[::-1], file=open('output.txt', 'w'))
