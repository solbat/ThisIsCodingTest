# 예제 4-1 상하좌우

n = int(input())
directions = input().split()

pos = [1, 1]

def move(d):
    if d == 'L':
        if pos[1] != 1:
            pos[1] -= 1
    elif d == 'R':
        if pos[1] != n:
            pos[1] += 1
    elif d == 'U':
        if pos[0] != 1:
            pos[0] -= 1
    elif d == 'D':
        if pos[0] != n:
            pos[0] += 1

for d in directions:
    move(d)

print(pos[0], pos[1])


# ##########

# # 4-1.py 답안 예시

# # N을 입력받기
# n = int(input())
# x, y = 1, 1
# plans = input().split()

# # L, R, U, D에 따른 이동 방향
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']

# # 이동 계획을 하나씩 확인
# for plan in plans:
#     # 이동 후 좌표 구하기
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#         # 공간을 벗어나는 경우 무시
#         if nx < 1 or ny < 1 or nx > n or ny > n:
#             continue
#         # 이동 수행
#         x, y = nx, ny

# print(x, y)