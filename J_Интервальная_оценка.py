import numpy as np
import scipy
from scipy import stats

fr = open('input.txt', 'r')

n, confidence = map(float, fr.readline().split())

x = np.array(list(map(float, fr.readline().split())))
y = np.array(list(map(float, fr.readline().split())))

# numerator = np.sum((x - np.mean(x)) * (y - np.mean(y)))
# denominator = np.sum((x - np.mean(x))**2)
#
# if denominator == 0 or numerator == 0:
#     open('output.txt', 'w').write(str(0) + ' ' + str(0))
#     exit(0)
#
# a = numerator / denominator
# b = np.mean(y) - a * np.mean(x)

b1 = (sum(x*y) - (1/n) * sum(x) * sum(y)) / (sum(x**2) - (1/n) * sum(x)**2)
b0 = (1/n) * sum(y) - b1 * (1/n) * sum(x)

s_2 = (1/(n - 2)) * sum((y - b0 - b1 * x)**2)
s = s_2**(0.5)
s_b1 = s / sum((x - np.mean(x))**2)**(0.5)
s_b0 = s / n**(0.5)
t = abs(stats.t.interval(confidence, n-2)[0])

fw = open('output.txt', 'w')
print(b0 - t*s_b0, b0 + t*s_b0, b1 - t*s_b1, b1 + t*s_b1, file=fw)



