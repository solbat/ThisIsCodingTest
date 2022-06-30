# ch11-Q01 모험가 길드

n = int(input())
data = list(map(int, input().split()))

data.sort()

count = 0
result = 0

for v in data:
    count += 1
    if count >= v:
        result += 1
        count = 0

print(result)