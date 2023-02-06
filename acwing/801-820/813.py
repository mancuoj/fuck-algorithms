def print2D(a, row, col):
    for i in range(row):
        for j in range(col):
            print(a[i][j], end=" ")
        print()


row, col = map(int, input().split())

a = []
for _ in range(row):
    a.append(list(map(int, input().split())))
print2D(a, row, col)
