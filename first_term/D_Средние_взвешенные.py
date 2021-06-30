from operator import mul

f = open('input.txt', 'r')
n = int(f.readline())

arr = []

for i in range(n):
    a, b = map(float, f.readline().split())
    arr += [a for _ in range(int(b))]

fw = open('output.txt', 'w')

fw.write(str(sum(arr) / len(arr)) + ' ')
fw.write(str(len(arr) / sum(map(lambda x: 1 / x, arr))) + ' ')
m = 1
for i in arr:
    m *= i
print(m)
fw.write(str(m**(1/len(arr)) ))
fw.close()
