n = int(input())

l = [0, 1, 1]
for i in range(3, n + 1):
    l.append(l[i - 1] + l[i - 2])
print(f"{l[n]:.2f}")
