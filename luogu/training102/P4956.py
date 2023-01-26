# (7x + 21k) * 52 = 364x + 1092k = n
n = int(input())

n /= 52
k = 1
while not (n % 7 == 0 and (n - 21 * k) / 7 <= 100):
    k += 1
print(int((n - 21 * k) / 7))
print(k)
