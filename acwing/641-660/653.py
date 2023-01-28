n = int(input())
values = [100, 50, 20, 10, 5, 2, 1]

print(n)
for i in values:
    print(f"{n // i} nota(s) de R$ {i},00")
    n %= i
