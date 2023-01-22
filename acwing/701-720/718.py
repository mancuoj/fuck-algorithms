n = int(input())

c, r, f, sum = 0, 0, 0, 0
for _ in range(n):
    x, y = input().split()
    x = int(x)
    sum += x
    if y == "C":
        c += x
    elif y == "R":
        r += x
    else:
        f += x

print(f"Total: {sum} animals")
print(f"Total coneys: {c}")
print(f"Total rats: {r}")
print(f"Total frogs: {f}")
print(f"Percentage of coneys: {c / sum * 100:.2f} %")
print(f"Percentage of rats: {r / sum * 100:.2f} %")
print(f"Percentage of frogs: {f / sum * 100:.2f} %")
