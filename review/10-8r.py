# ch10-3 실전 문제 : 도시 분할 계획

# import sys
# input = sys.stdin.readline

# 집의 개수 n, 길의 개수 m
n, m = map(int, input().split())

parent = [0] * (n + 1)
for i in range(n+1):
    parent[i] = i

edges = []
answer = 0
count = 0

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    c, a, b = edge
    if count == (n-2):
        break
    if parent[a] != parent[b]:
        union_parent(parent, a, b)
        answer += c
        count += 1
    else:
        continue

print(answer)