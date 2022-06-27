maze = []

for i in range(10):
    inputMaze = list(map(int,input().split()))
    maze.append(inputMaze)

# 시작 지점 설정
nowPoint = {'x': 1, 'y': 1}

while True:
    # 현재 위치에 쿠키가 있는지 검사
    if maze[nowPoint['x']][nowPoint['y']] == 2:
        maze[nowPoint['x']][nowPoint['y']] = 9
        break

    # 현재 개미의 자리에 9 표시
    maze[nowPoint['x']][nowPoint['y']] = 9

    # 다음 목적지 탐색
    if maze[nowPoint['x']][nowPoint['y']+1] == 1:
        if maze[nowPoint['x']+1][nowPoint['y']] == 1:
            break
        nowPoint['x'] += 1
    else:
        nowPoint['y'] += 1

for i in range(len(maze)):
    for j in range(len(maze)):
        print(maze[i][j], end=' ')
    print()