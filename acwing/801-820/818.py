n, l, r = map(int, input().split())
a = list(map(int, input().split()))

a = a[:l] + sorted(a[l : r + 1]) + a[r + 1 :]
for i in a:
    print(i, end=" ")
