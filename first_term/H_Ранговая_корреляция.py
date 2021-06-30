from scipy.stats import kendalltau

fr = open('input.txt', 'r')

sign = lambda x: x and (1, -1)[x<0]

n, m = map(int, fr.readline().split())

a = []

for _ in range(n):
    a.append(list(map(int, fr.readline().split())))

fw = open('output.txt', 'w')

ans = [[0 for _ in range(n)] for __ in range(n)]

for k in range(n):
    for h in range(k, n):
        # s = .0
        # for i in range(m-1):
        #     for j in range(i+1, m):
        #         s += sign(a[k][j]-a[k][i]) * sign(a[h][j]-a[h][i])
        coef, p = kendalltau(a[k], a[h])
        # coef = (2/(m*m - m)) * s
        ans[k][h] = coef
        ans[h][k] = coef

for i in ans:
    for j in i:
        fw.write(str(j) + ' ')
    fw.write('\n')
