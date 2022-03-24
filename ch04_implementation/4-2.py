# 예제 4-2 시각

n = int(input())

count = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            t = str(h)+str(m)+str(s)
            if '3' in t:
                count += 1

print(count)