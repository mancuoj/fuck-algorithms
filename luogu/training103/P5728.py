n = int(input())

l, s = [], []
for i in range(n):
    l.append(list(map(int, input().split())))
    s.append(sum(l[i]))

cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if (
            abs(s[i] - s[j]) <= 10
            and abs(l[i][0] - l[j][0]) <= 5
            and abs(l[i][1] - l[j][1]) <= 5
            and abs(l[i][2] - l[j][2]) <= 5
        ):
            cnt += 1
print(cnt)
