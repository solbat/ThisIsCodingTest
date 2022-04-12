# ch08-3 실전 문제 : 개미 전사

n = int(input())
foodStorage = list(map(int, input().split()))

maxFood = [0] * n

maxFood[0] = foodStorage[0]
maxFood[1] = max(foodStorage[0], foodStorage[1]) # 실수 주의! maxFood[1]은 인덱스 0과 1 둘 중에 최댓값이다!

for i in range(2, n):
    maxFood[i] = max(maxFood[i-1], maxFood[i-2]+foodStorage[i])

print(maxFood[n-1])