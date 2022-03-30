# 실전 문제 6-11 성적이 낮은 순서로 학생 출력하기

n = int(input())

data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    data.append((name, score))

data.sort(key = lambda x : x[1])

for student in data:
    print(student[0], end=' ')