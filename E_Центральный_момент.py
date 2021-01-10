f = open('input.txt', 'r')
n, k = map(int, f.readline().split())
a = list(map(float, f.read().split()))
mean = sum(a) / n

s = 0

for i in a:
    s += (i - mean)**k

open('output.txt', 'w').write(str(((1/n) * s)))
