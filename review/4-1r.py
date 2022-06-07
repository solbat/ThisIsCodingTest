# ch04-1 예제 : 상하좌우

# 공간의 크기 n 입력
n = int(input())
# 여행가 A가 이동할 계획서 내용 입력
data = list(input().split())
#### list() 함수 안써도 됨

# 여행가 A의 초기 위치 좌표
x, y = 1, 1

# L R U D 방향을 인덱스화 시키는 사전
pton = {"L":0, "R":1, "U":2, "D":3}

# 인덱스에 따른 x, y 좌표 변화
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 이동
for d in data:
    # 방향 인덱스 추출
    direction = pton[d]
    # 나아갈 방향
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 바운더리 확인
    if nx != 0 and ny != 0 and nx <= n and ny <= n:
        x = nx
        y = ny
    #### 바운더리 확인 깔끔하게
    #### if (공간을 벗어나는 조건) : continue
    #### else : x, y = nx, ny

print(x, y)