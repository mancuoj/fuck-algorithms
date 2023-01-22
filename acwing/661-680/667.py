a, b = map(int, input().split())

if a > b:
    b += 24

if a == b:
    print("O JOGO DUROU 24 HORA(S)")
else:
    print(f"O JOGO DUROU {b - a} HORA(S)")
