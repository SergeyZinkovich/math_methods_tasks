data = sorted(map(int, open('input.txt', 'r').read().split()[1:]))

f = open('output.txt', 'w')
    
d = {}

for i in data:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

f.write(' '.join(map(str, d.keys())))
f.write('\n')
f.write(' '.join(map(str, d.values())))
f.write('\n')
f.write(' '.join(map(str, [i / len(data) for i in d.values()])))
f.close()
