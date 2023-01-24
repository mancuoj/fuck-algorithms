c = input()

for i in range(3):
    for _ in range(2 - i):
        print(" ", end="")
    for _ in range(1 + 2 * i):
        print(c, end="")
    print()
