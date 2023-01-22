n = float(input())

if n > 100:
    print("Fora de intervalo")
elif n > 75:
    print("Intervalo (75,100]")
elif n > 50:
    print("Intervalo (50,75]")
elif n > 25:
    print("Intervalo (25,50]")
elif n >= 0:
    print("Intervalo [0,25]")
else:
    print("Fora de intervalo")
