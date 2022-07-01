# ch03-2 실전 문제 : 큰 수의 법칙

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

quotient = m // (k+1)
remainder = m % (k+1)

result = (first*k+second)*quotient + remainder*first

print(result)