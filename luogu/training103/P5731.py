n = int(input())
ans = [[0 for _ in range(n)] for _ in range(n)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
x, y, d = 0, 0, 1

for i in range(n * n):
    ans[x][y] = i + 1
    a, b = x + dx[d], y + dy[d]
    if a < 0 or a >= n or b < 0 or b >= n or ans[a][b]:
        d = (d + 1) % 4
        a, b = x + dx[d], y + dy[d]
    x, y = a, b

for i in range(n):
    for j in range(n):
        print(f"{ans[i][j]:3d}", end="")
    print()
