a, b, c, d = map(int, input().split())

if a >= c and b > d:
    c += 24
if b > d:
    d += 60
    c -= 1

if a == c and b == d:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print(f"O JOGO DUROU {c - a} HORA(S) E {d - b} MINUTO(S)")
