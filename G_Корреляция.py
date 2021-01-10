import numpy

fr = open('input.txt', 'r')
n = int(fr.readline().split()[0])

a = [list(map(float, fr.readline().split())) for _ in range(n)]

f = open('output.txt', 'w')

for i in numpy.corrcoef(numpy.array(a)):
    f.write(' '.join(map(lambda x: '%.3f' % x, i)) + '\n')

f.close()