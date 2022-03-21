# 실전 문제 3-4 1이 될 때까지

n, k = map(int, input().split())
result = 0

while(True):
    if n>=k:
        t = n%k
        result += t
        n -= t
        n /= k
        result += 1
    else:
        n -= 1
        result += 1
    
    if n==1:
        break

result = int(result)
print(result)