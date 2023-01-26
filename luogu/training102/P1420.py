n = int(input())
l = list(map(int, input().split()))

cnt, max = 0, 0
for i in range(1, n):
    if l[i] - l[i - 1] == 1:
        cnt += 1
    else:
        cnt = 0
    if cnt > max:
        max = cnt
print(max + 1)
