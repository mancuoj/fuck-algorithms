total = 0
for _ in range(2):
    x, y, z = input().split()
    total += int(y) * float(z)
print(f"VALOR A PAGAR: R$ {total:.2f}")
