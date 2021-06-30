import numpy as np

f = open('input.txt', 'r')
n, m, k = map(int, f.readline().split())
data = list(map(float, f.readline().split()))

last = []

for i in range(k):
    last.append(data[-1])
    data = np.diff(data)

test = np.zeros((n-k-m, m+1))
test[:, 0] = 1
for i in range(n-k-m):
    for j in range(m):
        test[i][j+1] = data[i + j]


coeff = np.linalg.lstsq(test, data[m:])[0]

y_n_1 = coeff[0]
y_n_1 += sum(data[n-m-k:n] * coeff[1:])

y_n_1 += sum(last)

open('output.txt', 'w').write(str(y_n_1))
