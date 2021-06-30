a = list(map(float, open('input.txt', 'r').read().split()[1:]))
open('output.txt', 'w').write(str(len(a) / sum(map(lambda x: 1 / x, a))))
