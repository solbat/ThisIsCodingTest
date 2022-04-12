# ch08-5 실전 문제 : 효율적인 화폐 구성

# N, M 입력받기
n, m = map(int, input().split())

# N개의 줄에 각 화폐의 가치 입력받기
mlist = []
for i in range(n):
    mlist.append(int(input()))

# 금액에 따른 최소한의 화폐 개수를 저장하는 배열
INF = 10001
d = [INF] * 10001

# 기본 화폐 단위에 해당하는 금액에 1개 부여
for i in mlist:
    d[i] = 1

for i in range(1, m+1):
    for j in mlist:
        if (i-j) > 0:
            d[i] = min(d[i], d[i-j]+1)

if d[m] < INF:
    print(d[m])
else:
    print(-1)
