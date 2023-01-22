n = float(input())
n *= 100
values = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
sign = "nota"

print("NOTAS:")
for i in range(len(values)):
    if values[i] == 100:
        print("MOEDAS:")
        sign = "moeda"
    print(f"{int(n // values[i])} {sign}(s) de R$ {values[i] / 100:.2f}")
    n %= values[i]
