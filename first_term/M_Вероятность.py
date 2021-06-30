def probability(pdf, a, b):
    n = 1000
    ans = 0
    for i in range(n):
        ans += pdf(a + i * (b-a) / n)
    return ans * (b - a) / n