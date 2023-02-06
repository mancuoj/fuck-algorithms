x, y = int(input()), int(input())

if x > y:
    x, y = y, x

total = 0
for i in range(x + 1, y):
    if i % 2 != 0:
        total += i
print(total)
