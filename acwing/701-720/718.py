n = int(input())

c, r, f, total = 0, 0, 0, 0
for _ in range(n):
    x, y = input().split()
    x = int(x)
    total += x
    if y == "C":
        c += x
    elif y == "R":
        r += x
    else:
        f += x

print(f"Total: {total} animals")
print(f"Total coneys: {c}")
print(f"Total rats: {r}")
print(f"Total frogs: {f}")
print(f"Percentage of coneys: {c / total * 100:.2f} %")
print(f"Percentage of rats: {r / total * 100:.2f} %")
print(f"Percentage of frogs: {f / total * 100:.2f} %")
