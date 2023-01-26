s = input()

if s == "0":
    print(0)
else:
    if s[0] == "-":
        s = s[1:]
        print("-", end="")

    s = s[::-1]
    while s[0] == "0":
        s = s[1:]
    print(s)
