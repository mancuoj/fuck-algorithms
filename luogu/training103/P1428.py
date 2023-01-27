n = int(input())
l = list(map(int, input().split()))

x = [0]
for i in range(1, n):
    cnt = 0
    for j in range(i):
        if l[j] < l[i]:
            cnt += 1
    x.append(cnt)

for i in range(n):
    print(x[i], end=" ")
