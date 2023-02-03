s = input()

for i in s:
    if "a" <= i < "z" or "A" <= i < "Z":
        print(chr(ord(i) + 1), end="")
    elif i == "z":
        print("a", end="")
    elif i == "Z":
        print("A", end="")
    else:
        print(i, end="")
