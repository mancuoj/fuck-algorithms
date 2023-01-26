n = int(input())

price = 0
if n > 400:
    price += (n - 400) * 0.5663
    n = 400
if n > 150:
    price += (n - 150) * 0.4663
    n = 150
price += n * 0.4463

print(f"{price:.1f}")
