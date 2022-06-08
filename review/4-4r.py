# ch04-4 실전 문제 : 게임 개발

# 맵 크기 nxm 입력
n, m = map(int, input().split())

# 현재 위치 x, y, 방향 d 입력
x, y, d = map(int, input().split())

# 맵 구조 입력
array = []
for i in range(n):
    row = list(map(int, input().split()))
    array.append(row)

# 방문 여부 확인
check = [[0]*m for i in range(n)]

# 다음 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 첫 시작
check[x][y] = 1
turn = 0

while(True):
    turn += 1
    d = (d+3)%4
    nx = x + dx[d]
    ny = y + dy[d]

    if check[nx][ny] != 1 and array[nx][ny] != 1:
        x = nx
        y = ny
        check[x][y] = 1
        turn = 0
    
    if turn == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if array[nx][ny] == 1:
            break
        else:
            x = nx
            y = ny
            turn = 0

# 방문한 칸의 수 세기
count = 0
for row in check:
    for v in row:
        if v == 1:
            count += 1

print(count)