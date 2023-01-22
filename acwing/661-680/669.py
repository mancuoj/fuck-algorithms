n = float(input())

increase = [4, 7, 10, 12, 15]
if n > 2000:
    sign = 0
elif n > 1200:
    sign = 1
elif n > 800:
    sign = 2
elif n > 400:
    sign = 3
else:
    sign = 4

inc = n * increase[sign] / 100
print(f"Novo salario: {n + inc:.2f}")
print(f"Reajuste ganho: {inc:.2f}")
print(f"Em percentual: {increase[sign]} %")
