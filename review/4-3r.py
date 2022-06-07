# ch04-3 실전 문제 : 왕실의 나이트

p = input()

# 체스판 위치를 좌표화
x = int(p[1])
y = ord(p[0]) - ord('a') + 1

# 이동 가능한 스텝
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
#### steps = [(-2, -1), (-1, -2), (1, -2), ...] 이런 식으로도 표현 가능

# 이동 후 가능한 위치 후보들
candidate = []

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    candidate.append((nx, ny))
#### candidate 굳이 공간 낭비

# 가능한 위치 카운트
count = 0

for p in candidate:
    if p[0] > 0 and p[0] <= 8 and p[1] > 0 and p[1] <= 8:
        count += 1

print(count)