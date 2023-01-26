k = int(input())

ans, day, cnt = 0, 0, 1
for i in range(1, k + 1):
    ans += cnt
    day += 1
    if day == cnt:
        day = 0
        cnt += 1
print(ans)
