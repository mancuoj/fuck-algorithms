n = int(input())
l = list(map(int, input().split()))

min = l[0]
for i in range(1, n):
    if l[i] < min:
        min = l[i]
print(min)
