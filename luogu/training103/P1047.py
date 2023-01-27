l, m = map(int, input().split())

ans = [0 for _ in range(l + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    for i in range(u, v + 1):
        ans[i] = 1
print(ans.count(0))
