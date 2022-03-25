# 실전 문제 4-4 게임 개발

# 맵 크기 N, M 입력
n, m = map(int, input().split())

# 시작 위치 및 방향 x, y, d 입력
x, y, d = map(int, input().split())

# 맵 모양 입력
map_list = []
for i in range(n):
    row = list(map(int, input().split()))
    map_list.append(row)

# 맵 방문 정보 저장
map_visited = [[0] * m for _ in range(n)]

# 방향에 따른 dx, dy 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0
explore = 0

# 시작
map_visited[x][y] = 1
count += 1

while(True):
    # 우선 turn
    d = (d+3)%4

    # 갈 수 있는지 판단
    # 바다 아니고 방문한 적 없다면 가자
    if (map_list[x+dx[d]][y+dy[d]] == 0) & (map_visited[x+dx[d]][y+dy[d]] == 0):
        x = x + dx[d]
        y = y + dy[d]
        map_visited[x][y] = 1
        count += 1
        explore = 0
    # 바다이거나 방문한 적이 있다면
    else:
        explore += 1
        # 사방이 막혀있을때(바다이거나 방문한 적 있다면)
        if explore == 4:
            # 뒤로 갈 수 있는지 판단
            nx = x - dx[d]
            ny = y - dy[d]
            # 뒤로 갈 수 있다면(바다가 아니라면)
            if map_list[nx][ny] == 0:
                x = nx
                y = ny
                explore = 0
            # 뒤로 갈 수 없다면(뱌다라면)
            else:
                print(count)
                break


# ##########

# # 4-4.py 답안 예시

# # N, M을 공백으로 구분하여 입력받기
# n, m = map(int, input().split())

# # 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
# d = [[0] * m for _ in range(n)]
# # 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
# x, y, direction = map(int, input().split())
# d[x][y] = 1 # 현재 좌표 방문 처리

# # 전체 맵 정보를 입력받기
# array = []
# for i in range(n):
#     array.append(list(map(int, input().split())))

# # 북, 동, 남, 서 방향 정의
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# # 왼쪽으로 회전
# def turn_left():
#     global direction # global 키워드 사용. 정수형 변수인 direction 변수가 함수 바깥에서 선언된 전역변수이기 때문.
#     direction -= 1
#     if direction == -1:
#         direction = 3

# # 시뮬레이션 시작
# count = 1
# turn_time = 0
# while True:
#     # 왼쪽으로 회전
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#     # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
#     if d[nx][ny] == 0 and array[nx][ny] == 0:
#         d[nx][ny] = 1
#         x = nx
#         y = ny
#         count += 1
#         turn_time = 0
#         continue
#     # 회전한 이후 정면에 가보지 않은칸이 없거나 바다인 경우
#     else:
#         turn_time += 1
#     # 네 방향 모두 갈 수 없는 경우
#     if turn_time == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]
#         # 뒤로 갈 수 있다면 이동하기
#         if array[nx][ny] == 0:
#             x = nx
#             y = ny
#         # 뒤가 바다로 막혀있는 경우
#         else:
#             break
#         turn_time = 0

# # 정답 출력
# print(count)