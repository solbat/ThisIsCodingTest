# ch07-2 실전 문제 : 부품 찾기

n = int(input())
stocks = list(map(int, input().split()))
# stocks = set(map(int, input().split()))

m = int(input())
requests = list(map(int, input().split()))


## 방법 1 : set 혹은 list으로 in 활용
for request in requests:
    if request in stocks:
        print('YES', end=' ')
    else:
        print('NO', end=' ')


## 방법 2 : 이진 탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

# 이진 탐색의 전제조건 : 오름차순 정렬
stocks.sort()

for request in requests:
    if binary_search(stocks, request, 0, n-1) != None:
        print('YES', end=' ')
    else:
        print('NO', end=' ')


## 방법 3 : 계수 정렬
array = [0] * 1000001
for stock in stocks:
    array[stock] = 1

for request in requests:
    if array[request] == 1:
        print('YES', end=' ')
    else:
        print('NO', end=' ')