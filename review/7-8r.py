# ch07-3 실전 문제 : 떡볶이 떡 만들기

# 떡의 개수 n, 요청한 떡의 길이 m
n, m = map(int, input().split())

# 떡의 개별 높이
data = list(map(int, input().split()))

def cut(array, length):
    sumOfDduk = 0
    for dduk in array:
        cut = dduk-length
        if cut > 0:
            sumOfDduk += cut
    return sumOfDduk

# 이진 탐색 : 종료조건, mid
def binary_search(array, target, start, end):
    result = 0
    while start <= end:
        mid = (start+end) // 2
        sumOfDduk = cut(array, mid)
        if sumOfDduk < target:
            end = mid - 1
        else:
            result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
            start = mid + 1
    return result

print(binary_search(data, m, 0, max(data)))