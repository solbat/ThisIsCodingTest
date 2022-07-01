# ch11-Q05 볼링공 고르기

from itertools import combinations

n, m = map(int, input().split())
weights = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(i+1, n):
        if weights[i] != weights[j]:
            count += 1

print(count)
