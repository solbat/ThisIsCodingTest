# ch05-4 실전 문제 : 미로 탈출

from collections import deque

# 직사각형 미로 크기 n X m 입력
n, m = map(int, input().split())

# 미로 정보 입력
maze = []
maze.append([0]*(m+1))
for i in range(n):
    maze.append([0]+list(map(int, input())))

# 방문 여부 확인
visited = [[0]*(m+1) for i in range(n+1)]

# 다음 갈 곳 스텝 : 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# BFS
#### + 새로운 아이디어
start = (1, 1)
count = 0

queue = deque([start])
visited[start[0]][start[1]] = 1
while queue:
    v = queue.popleft()
    #### 튜플 그대로 받지말고 원소별로 나눠받아
    #### x, y = queue.popleft()
    for i in range(4):
        nx = v[0] + dx[i]
        ny = v[1] + dy[i]
        if nx >= 1 and nx <= n and ny >= 1 and ny <= m and maze[nx][ny] != 0 and visited[nx][ny] == 0:
            queue.append((nx, ny))
            visited[nx][ny] = 1
            maze[nx][ny] = maze[v[0]][v[1]] + 1

print(maze[n][m])