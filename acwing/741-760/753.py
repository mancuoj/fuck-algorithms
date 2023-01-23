while True:
    n = int(input())
    if n == 0:
        break

    ans = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i, n - i):
            ans[i][j] = ans[j][i] = ans[n - 1 - i][j] = ans[j][n - 1 - i] = i + 1

    for i in range(n):
        for j in range(n):
            print(ans[i][j], end=" ")
        print()
    print()
