n, m = map(int, input().split())

ans = [[0 for _ in range(m)] for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  # 上下左右

x, y, d = 0, 0, 1
for i in range(n * m):
    ans[x][y] = i + 1
    a, b = x + dx[d], y + dy[d]  # 走一步
    if a < 0 or a >= n or b < 0 or b >= m or ans[a][b]:
        d = (d + 1) % 4  # 转九十度，再走一步
        a, b = x + dx[d], y + dy[d]
    x, y = a, b

for i in range(n):
    for j in range(m):
        print(ans[i][j], end=" ")
    print()
