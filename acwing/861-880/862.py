n = int(input())

l = []
for i in range(n):
    l.append(input().split())

for i in sorted(l, key=lambda el: int(el[0])):
    print(" ".join(i))
