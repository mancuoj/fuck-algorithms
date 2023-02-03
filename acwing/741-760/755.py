while True:
    n = int(input())
    if n == 0:
        break

    ans = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            print(2 ** (i + j), end=" ")
        print()
    print()
