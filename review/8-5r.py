# ch08-2 실전 문제 : 1로 만들기

x = int(input())

array = [0] * 150000

for i in range(1, x+1):
    array[i*5] = array[i] + 1 if array[i*5] == 0 else min(array[i*5], array[i] + 1)
    array[i*3] = array[i] + 1 if array[i*3] == 0 else min(array[i*3], array[i] + 1)
    array[i*2] = array[i] + 1 if array[i*2] == 0 else min(array[i*2], array[i] + 1)
    array[i+1] = array[i] + 1 if array[i+1] == 0 else min(array[i+1], array[i] + 1)

print(array[x])

for i, v in enumerate(array[:x+1]):
    print(i, v)
