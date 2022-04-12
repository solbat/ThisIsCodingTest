# ch08-2 실전 문제 : 1로 만들기

x = int(input())
INF = 987654321

array = [INF] * (x*5+1)
array[1] = 0

for i in range(1, x):
    n = array[i]
    a = array[i*5]
    b = array[i*3]
    c = array[i*2]
    d = array[i+1]

    if ((n+1) < a):
        array[i*5] = n+1
    if ((n+1) < b):
        array[i*3] = n+1
    if ((n+1) < c):
        array[i*2] = n+1
    if ((n+1) < d):
        array[i+1] = n+1
    
print(array[x])