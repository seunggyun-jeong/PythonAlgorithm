h, w = map(int, input().split())

# 격자판 만들기
board = []

for i in range(h):
    board.append([])
    for _ in range(w):
        board[i].append(0)

# 막대 개수 입력
n = int(input())

# 막대 정보 입력
for _ in range(n):
    l, d, row, column = map(int, input().split())

    if d == 0:
        for i in range(l):
            board[row-1][column-1+i] = 1
    else:
        for i in range(l):
            board[row-1+i][column-1] = 1



# 결과 출력
for i in range(h):
    for j in range(w):
        print(board[i][j], end=' ')
    print()
