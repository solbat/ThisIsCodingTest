# ch06-3 실전 문제 : 성적이 낮은 순서로 학생 출력하기

# 학생의 수 n 입력
n = int(input())

array = []
for i in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))

array = sorted(array, key=lambda x:x[1])

for val in array:
    print(val[0], end=' ')