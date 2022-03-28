# 실전 문제 5-10 음료수 얼려 먹기

# 세로 길이 N, 가로 길이 M
n, m = map(int, input().split())

# 얼음 틀 입력
tray = []
for _ in range(n):
    tray.append(list(map(int, input())))

# DFS로 특정 노드 방문 후 연결된 모든 노드를 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if tray[x][y] == 0:
        # 해당 노드를 방문 처리
        tray[x][y] = 1
        # 상 하 좌 우 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    # 현재 노드가 방문되었다면
    return False

# 모든 위치에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)