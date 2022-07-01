# ch09-3 실전 문제 : 전보

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count = 0
max_distance = 0

for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)