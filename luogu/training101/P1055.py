a, b, c, x = input().split("-")
n = a + b + c
sign = "0123456789X"

sum = 0
for i in range(9):
    sum += int(n[i]) * (i + 1)

if sign[sum % 11] == x:
    print("Right")
else:
    print(f"{a}-{b}-{c}-{sign[sum % 11]}")
