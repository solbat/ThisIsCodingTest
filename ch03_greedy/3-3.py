# 실전 문제 3-3 큰 수의 법칙

N, M = map(int, input().split())
data = []
for i in range(N):
    row = list(map(int, input().split()))
    data.append(row)

rm = min(data[0])
al = []

for i in range(N):
    if rm < min(data[i]):
        rm = min(data[i])
    # print(rm)
    al.append(rm)

result = max(al)
print(result)


# ##########

# # min() 함수를 이용하는 답안 예시

# # N, M을 공백으로 구분하여 입력받기
# n, m = map(int, input().split())

# # 각 줄의 가장 작은 수가 모두 음수일 경우 result를 0으로 초기화하는 것에 문제가 있음
# result = 0
# # 한 줄씩 입력받아 확인
# for i in range(n):
#     data = list(map(int, input().split()))
#     # 현재 줄에서 '가장 작은 수' 찾기
#     min_value = min(data)
#     # '가장 작은 수'들 중에서 가장 큰 수 찾기
#     result = max(result, min_value)

# print(result) # 최종 답안 출력

# # 2중 반복문 구조를 이용하는 답안 예시