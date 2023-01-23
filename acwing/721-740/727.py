n = int(input())
x = int(n / 2)

for i in range(-x, x + 1):
    for _ in range(abs(i)):
        print(" ", end="")
    for _ in range(n - abs(i) * 2):
        print("*", end="")
    print()
