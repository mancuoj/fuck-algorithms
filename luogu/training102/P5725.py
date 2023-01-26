n = int(input())

cnt = 1
for _ in range(n):
    for _ in range(n):
        print(f"{cnt:02d}", end="")
        cnt += 1
    print()

print()

cnt = 1
for i in range(n):
    for _ in range(n - 1 - i):
        print("  ", end="")
    for _ in range(i + 1):
        print(f"{cnt:02d}", end="")
        cnt += 1
    print()
