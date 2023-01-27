n = int(input())
prize = list(map(int, input().split()))

cnt = [0 for _ in range(7)]
for _ in range(n):
    x = list(map(int, input().split()))
    s = 0
    for i in range(7):
        if prize.count(x[i]) == 1:
            s += 1
    if s > 0:
        cnt[7 - s] += 1

for i in range(7):
    print(cnt[i], end=" ")
