# 실전 문제 7-5 부품 찾기

# 부품 재고 개수와 고유 번호 입력받기
n = int(input())
stock = list(map(int, input().split()))

# 문의한 부품 개수와 고유 번호 입력받기
m = int(input())
request = list(map(int, input().split()))

# 부품 재고 번호 오름차순 정렬
stock.sort()

def binary_search(array, target, start, end):
    while start<=end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

# 각 요소에 대하여 이진 탐색 진행
for i in request:
    result = binary_search(stock, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')