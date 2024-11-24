import numpy as np

p = np.array([0 , 1 , 2, 5, 6])
wt = np.array([0 , 2 , 3, 4, 5])
m = 8
n = 4

k = np.zeros((n + 1, m + 1))

for i in range(n):
    for j in range(m):
        if wt[i - 1] <= j:
            k[i , j] = max(p[i] + k[i - 1, j - wt[i]], k[i - 1, j])

        else:
            k[i, j] = k[i-1 , j]

print(k)

while (i > 0 and j > 0):
    if k[i , j] == k[i - 1, j]:
        print(i, '= 0')
        i -= 1
    else:
        print(i , '= 1')
        j = j - wt[i]
        i -= 1



