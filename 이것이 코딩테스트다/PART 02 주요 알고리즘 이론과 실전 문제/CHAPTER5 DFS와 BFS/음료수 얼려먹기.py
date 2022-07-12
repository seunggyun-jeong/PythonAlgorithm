n, m = map(int, input().split())
iceTable = []

for i in range(n):
    line = list(map(int, input()))
    iceTable.append(line)

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if iceTable[x][y] == 0:
        iceTable[x][y] = 1
        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x - 1, y)
        return True
    return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
