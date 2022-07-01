# ch10-4 실전 문제 : 커리큘럼

# 듣고자 하는 강의의 수 n
n = int(input())

lectures = [[]]

answer = [0] * (n+1)

for i in range(n):
    lectures.append(list(map(int, input().split())))

for i in range(1, n+1):
    p = 0
    for v in lectures[i][1:-1]:
        p = max(answer[v], p)
    answer[i] = lectures[i][0] + p

for i in range(1, n+1):
    print(answer[i])