a = list(map(float, open('input.txt', 'r').read().split()[1:]))
open('output.txt', 'w').write(str(sum(a) / len(a)))
