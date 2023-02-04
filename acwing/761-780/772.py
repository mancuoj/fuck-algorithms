s = input()

l = [0] * 26
for i in s:
    l[ord(i) - 97] += 1

for i in s:
    if l[ord(i) - 97] == 1:
        print(i)
        break
else:
    print("no")
