list = list(map(int, input().split()))

a = list[0]
for i in range(1, len(list)):
    if list[i] > 0:
        n = list[i]
        break

total = 0
for i in range(a, a + n):
    total += i
print(total)
