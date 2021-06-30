import numpy as np

fr = open('input.txt', 'r')

n = int(fr.readline())

a = []

for _ in range(n):
    a.append(list(map(float, fr.readline().split())))

a = np.array(a)

c = np.linalg.eig(a)
id = c[0].argsort()[::1]

fw = open('output.txt', 'w')

fw.write(' '.join(map(str, c[0][id])))
fw.write('\n')
fw.write('\n'.join(map(lambda x: ' '.join(map(str, x)), c[1][:, id].T)))

