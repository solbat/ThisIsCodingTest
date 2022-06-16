# ch08-5 실전 문제 : 효율적인 화폐 구성

n, m = map(int, input().split())
money = []
for i in range(n):
    money.append(int(input()))

money.sort()

count = [0] * (m + 1 + money[n-1])
for val in money:
    count[val] = 1

for i in range(1, m+1):
    if count[i] != 0:
        for val in money:
            count[i+val] = count[i] + 1 if count[i+val] == 0 else min(count[i] + 1, count[i+val])
            # if count[i+val] == 0:
            #     count[i+val] = count[i] + 1
            # else:
            #     count[i+val] = min(count[i] + 1, count[i+val])

if count[m] != 0:
    print(count[m])
else:
    print('-1')

print(count)
print(len(count))