from math import sqrt, pow

x = int(input())

if x == 1:
    print("I love Luogu!")
elif x == 2:
    print("6 4")
elif x == 3:
    print(3)
    print(12)
    print(2)
elif x == 4:
    print(f"{500 / 3:.6g}")  # g 有效位，float 默认为 6
elif x == 5:
    print(int((220 + 260) / (20 + 12)))
elif x == 6:
    print(f"{sqrt(6 * 6 + 9 * 9):.6g}")
elif x == 7:
    print(110)
    print(90)
    print(0)
elif x == 8:
    print(f"{2 * 3.141593 * 5:.6g}")
    print(f"{3.141593 * 5 * 5:.6g}")
    print(f"{4 * 3.141593 * 5 * 5 * 5 / 3:.6g}")
elif x == 9:
    print(22)
elif x == 10:
    print(9)
elif x == 11:
    print(f"{100 / 3:.6g}")
elif x == 12:
    print(13)
    print("R")
elif x == 13:
    print(int(pow(4 * 3.141593 * 1064 / 3, 1 / 3)))
elif x == 14:
    print(50)
