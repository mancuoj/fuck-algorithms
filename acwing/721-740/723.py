n, m = map(int, input().split())

cnt = 1
for _ in range(n):
    for _ in range(m):
        if cnt % m == 0:
            print("PUM", end=" ")
        else:
            print(cnt, end=" ")
        cnt += 1
    print()
