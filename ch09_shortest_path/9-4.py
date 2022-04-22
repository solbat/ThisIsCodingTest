# ch09-2 실전 문제 : 미래 도시

# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9)

# 전체 회사의 개수 N, 경로의 개수 M 입력받기
n, m = map(int, input().split())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

# 연결된 두 회사의 번호 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 최종 목적지 노드 X와 거쳐 갈 노드 K 입력받기
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1을 출력
if distance >= INF:
    print("-1")
# 도달할 수 있다면, 최단 거리를 출력
else:
    print(distance)
