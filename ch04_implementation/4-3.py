# 실전 문제 4-3 왕실의 나이트

alist = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

def aton(i):
    for index, alphabet in enumerate(alist):
        if i == alphabet:
            return index+1

rc = input()
x = int(rc[1])
y = aton(rc[0])

p1 = (x-2, y+1)
p2 = (x-1, y+2)
p3 = (x+1, y+2)
p4 = (x+2, y+1)
p5 = (x+2, y-1)
p6 = (x+1, y-2)
p7 = (x-1, y-2)
p8 = (x-2, y-1)

l = [p1, p2, p3, p4, p5, p6, p7, p8]
count = 0

for p in l:
    if (0<p[0]<9) & (0<p[1]<9):
        count += 1

print(count)


# ##########

# # 4-3.py 답안 예시

# # 현재 나이트 위치 입력받기
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1

# # 나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0
# for step in steps:
#     # 이동하고자 하는 위치 확인
#     next_row = row + step[0]
#     next_column = column + step[1]
#     # 해당 위치로 이동이 가능하다면 카운트 증가
#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#         result += 1

# print(result)