import numpy as np

fr = open('input.txt', 'r')

n, m = map(int, fr.readline().split())

a = []

for _ in range(n):
    a.append(list(map(float, fr.readline().split())))

a = np.array(a)

c = np.linalg.svd(a)

fw = open('output.txt', 'w')

fw.write('\n'.join(map(lambda x: ' '.join(map(str, x)), c[0])))
fw.write('\n')
fw.write('\n')

b = np.zeros((n, m))

for i in range(len(c[1])):
    b[i][i] = c[1][i]

fw.write('\n'.join(map(lambda x: ' '.join(map(str, x)), b)))
fw.write('\n')
fw.write('\n')

fw.write('\n'.join(map(lambda x: ' '.join(map(str, x)), c[2])))

