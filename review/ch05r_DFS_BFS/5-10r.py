# ch05-3 실전 문제 : 음료수 얼려 먹기

from collections import deque

# 얼음 틀 n X m 입력
n, m = map(int, input().split())

# 얼음 틀 형태 입력
data = []
for i in range(n):
    data.append(input())

# 연결 여부 나타내는 그래프(3차원? 리스트)
graph = [[[] for _ in range(m)] for _ in range(n)]
# 0, 1, 2, 3 : 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(n):
    for j in range(m):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                graph[i][j].append((nx, ny))

# 방문 여부 확인
visited = [[False]*m for i in range(n)]

# BFS
def BFS(graph, start, visited, data):
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        v = queue.popleft()
        for i in graph[v[0]][v[1]]:
            if not visited[i[0]][i[1]] and data[i[0]][i[1]] == '0':
                queue.append(i)
                visited[i[0]][i[1]] = True

# 아이스크림 카운드
count = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j] and data[i][j] == '0':
            BFS(graph, (i, j), visited, data)
            count += 1

print(count)