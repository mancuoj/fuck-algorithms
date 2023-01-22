sum = 0
for _ in range(2):
    x, y, z = input().split()
    sum += int(y) * float(z)
print(f"VALOR A PAGAR: R$ {sum:.2f}")
