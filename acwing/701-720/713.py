n = int(input())

cnt = 0
for _ in range(n):
    if 10 <= int(input()) <= 20:
        cnt += 1

print(cnt, "in")
print(n - cnt, "out")
