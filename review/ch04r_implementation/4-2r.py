# ch04 예제 4-2 : 시각

n = int(input())

count = 0

# h, m, s = n, 0, 0

# for i in range(n):
#     for j in range(60):
#         for k in range(60):

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count += 1

print(count)