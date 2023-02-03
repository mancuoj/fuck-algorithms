t = int(input())

for _ in range(t):
    a, b = input().split()
    if a == b:
        print("Tie")
    elif (
        (a == "Hunter" and b == "Gun")
        or (a == "Gun" and b == "Bear")
        or (a == "Bear" and b == "Hunter")
    ):
        print("Player1")
    else:
        print("Player2")
