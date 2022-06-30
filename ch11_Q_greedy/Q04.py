# ch11-Q04 만들 수 없는 금액

"""
from itertools import combinations

n = int(input())
coins = list(map(int, input().split()))

possible = set()

for i in range(1, n+1):
    temp = combinations(coins, i)
    for v in temp:
        possible.add(sum(v))

for v in range(1, int(1e9)):
    if v not in possible:
        print(v)
        break
"""

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)