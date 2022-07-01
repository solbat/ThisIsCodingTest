# ch06-2 실전 문제 : 위에서 아래로

# 수열 수의 개수 n 입력
n = int(input())

data = []
for i in range(n):
    data.append(int(input()))

data.sort(reverse=True)
#### array = sorted(array, reverse=True)

for val in data:
    print(val, end=' ')