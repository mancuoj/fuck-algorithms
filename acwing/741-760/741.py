n = int(input())

fib = []
fib += [0, 1]
for i in range(2, 61):
    fib.append(fib[i - 1] + fib[i - 2])

for _ in range(n):
    x = int(input())
    print(f"Fib({x}) = {fib[x]}")
