# ch11-Q02 곱하기 혹은 더하기

S = input()

result = 0

for num in S:
    temp = int(num)
    result = max((result + temp), (result * temp))

print(result)

# 두 수 중에서 하나라도 0 혹은 1인 경우, 곱하기보다는 더하기 수행