# ch08-4 실전 문제 : 바닥 공사

n = int(input())
array = [0] * (n+1)

array[1] = 1
array[2] = 3

for i in range(3, n+1):
    array[i] = array[i-1] + array[i-2]*2

print(array[n]%796796)