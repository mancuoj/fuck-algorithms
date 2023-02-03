k, a, b = float(input()), input(), input()

cnt = 0
for i in range(len(a)):
    if a[i] == b[i]:
        cnt += 1

if cnt / len(a) >= k:
    print("yes")
else:
    print("no")
