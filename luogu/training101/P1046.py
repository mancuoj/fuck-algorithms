l = list(map(int, input().split()))
x = int(input())

cnt = 0
for i in range(10):
    if x + 30 >= l[i]:
        cnt += 1
print(cnt)
