n = int(input())

l, mul = [0, 1], 1
for i in range(2, n + 1):
    mul *= i
    l.append(mul)

print(sum(l))
