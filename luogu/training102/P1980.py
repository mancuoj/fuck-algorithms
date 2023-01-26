n, x = map(int, input().split())

s = ""
for i in range(1, n + 1):
    s += str(i)
print(s.count(str(x)))
