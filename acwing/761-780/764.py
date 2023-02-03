a = input()

b = ""
for i in range(len(a) - 1):
    b += chr(ord(a[i]) + ord(a[i + 1]))
b += chr(ord(a[len(a) - 1]) + ord(a[0]))
print(b)
