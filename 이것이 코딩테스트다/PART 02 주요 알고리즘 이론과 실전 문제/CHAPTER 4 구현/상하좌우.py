# L, R, U, D를 입력 받을 때 최종적으로 도착할 좌표를 구하시오

n = int(input()) # 공간의 크기 입력
x, y = 1, 1
controller = input().split() # 사용자 입력 받음

for i in controller :
    if i == 'L':
        x -= 1
    elif i == 'R':
        x += 1
    elif i == 'U':
        y -= 1
    else:
        y += 1

print(x, y)

# 모범 답안
x, y = 1, 1
# 이동 관련 정의
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moveTypes = ['L', 'R', 'U', 'D']

# 이동 계획 확인
for plan in controller:
    # 이동 후 좌표 구하기
    for i in range(len(moveTypes)):
        if plan == moveTypes[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x = nx
    y = ny

print(x, y)
