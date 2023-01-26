from fractions import Fraction

a, b, c = map(int, input().split())
print(Fraction(min(a, b, c), max(a, b, c)))
