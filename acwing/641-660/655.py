n = int(input())

print(n // 365, "ano(s)")
print(n % 365 // 30, "mes(es)")
print(n % 365 % 30, "dia(s)")
