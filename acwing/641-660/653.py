n = int(input())
values = [100, 50, 20, 10, 5, 2, 1]

print(n)
for i in range(len(values)):
    print(f"{n // values[i]} nota(s) de R$ {values[i]},00")
    n %= values[i]
