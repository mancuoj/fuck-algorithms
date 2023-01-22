n = float(input())

tax = 0
if n > 4500:
    tax += (n - 4500) * 0.28
    n = 4500
if n > 3000:
    tax += (n - 3000) * 0.18
    n = 3000
if n > 2000:
    tax += (n - 2000) * 0.08

if tax > 0:
    print(f"R$ {tax:.2f}")
else:
    print("Isento")
