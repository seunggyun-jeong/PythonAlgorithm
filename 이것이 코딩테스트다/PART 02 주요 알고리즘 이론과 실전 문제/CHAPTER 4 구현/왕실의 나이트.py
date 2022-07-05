# 특정 위치에서 나이트가 이동할 수 있는 경우의 수를 구하시오
# 8 * 8 체스판

now = input()
nowRow = int(now[1])
nowCol = int(ord(now[0])) - int(ord('a')) + 1
knightPattern = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

count = 0

for pattern in knightPattern:
    if 8 >= (nowRow + pattern[1]) >= 1 and 1 <= nowCol + pattern[0] <= 8:
        count += 1

print(count)
