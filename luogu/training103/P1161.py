n = int(input())

l = [0 for _ in range(1000000)]
for _ in range(n):
    a, t = input().split()
    a = float(a)
    t = int(t)
    for i in range(1, t + 1):
        if l[int(i * a)] == 0:
            l[int(i * a)] = 1
        else:
            l[int(i * a)] = 0

for i in range(len(l)):
    if l[i] == 1:
        print(i)
        break
