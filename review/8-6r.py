# ch08-3 실전 문제 : 개미 전사

# 식량창고의 개수 n
n = int(input())
# 각 식량창고에 저장된 식량의 개수
array = list(map(int, input().split()))

# 메모이제이션
d = [0] * n
d[0], d[1] = array[0], array[1] #### 틀렸음!!!!

#### 이게 맞음!!!!
d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i-2]+array[i], d[i-1])

print(d[n-1])