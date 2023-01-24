x = int(input())

a, b = x % 2 == 0, 4 < x <= 12
print(f"{int(a & b)} {int(a | b)} {int(a ^ b)} {int(not a and not b)}")
