# 8-2.py 피보나치 수열 소스코드(재귀적)

import time

# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수(Fibonacci Function)를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo_dynamic(x):
    # 종료 조건(1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo_dynamic(x-1) + fibo_dynamic(x-2)
    return d[x]

# 피보나치 함수(Fibonacci Function)를 재귀 함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

# 다이나믹 프로그래밍으로 구현한 피보나치 시간 측정
s1 = time.time()
print(fibo_dynamic(30))
e1 = time.time()
t1 = e1 - s1

# 일반 재귀 함수로 구현한 피보나치 시간 측정
s2 = time.time()
print(fibo(30))
e2 = time.time()
t2 = e2 - s2

print('다이나믹 피보나치 : ' + str(t1))
print('재귀함수 피보나치 : ' + str(t2))