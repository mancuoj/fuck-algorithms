n, size = map(int, input().split())
a = list(map(int, input().split()))

for i in range(size // 2):
    a[i], a[size - 1 - i] = a[size - 1 - i], a[i]

for i in a:
    print(i, end=" ")
