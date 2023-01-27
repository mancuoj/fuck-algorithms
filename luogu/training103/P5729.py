w, x, h = map(int, input().split())
q = int(input())

ans = [[[0 for _ in range(20)] for _ in range(20)] for _ in range(20)]
cnt = 0
for _ in range(q):
    x1, y1, z1, x2, y2, z2 = map(int, input().split())
    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            for k in range(z1 - 1, z2):
                if ans[i][j][k] == 0:
                    ans[i][j][k] = 1
                    cnt += 1
print(w * x * h - cnt)
