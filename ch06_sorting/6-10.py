# 실전 문제 6-10 위에서 아래로

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

data.sort(reverse=True)

for i in range(len(data)):
    print(data[i], end=' ')

for i in data:
    print(i, end=' ')