# ch03-3 실전 문제 : 숫자 카드 게임

n, m = map(int, input().split())
result = 0
for _ in range(n):
    row = list(map(int, input().split()))
    min_num = min(row)
    result = max(result, min_num)

print(result)