a, b = map(int, input().split())

if b % a == 0 or a % b == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

# print("Sao Multiplos" if b % a == 0 or a % b == 0 else "Nao sao Multiplos")
