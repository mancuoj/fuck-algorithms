n = int(input())

cnt = 1
for i in range(n):
    for _ in range(n - i):
        print(f"{cnt:02d}", end="")
        cnt += 1
    print()
