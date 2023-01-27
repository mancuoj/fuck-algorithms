n = int(input())
ans = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    ans[i][0] = ans[i][i] = 1

for i in range(2, n):
    for j in range(1, i):
        ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]

for i in range(n):
    for j in range(i + 1):
        print(ans[i][j], end=" ")
    print()
