s = input().split()

s[-1] = s[-1][:-1]
max, max_s = 0, ""
for i in s:
    if len(i) > max:
        max = len(i)
        max_s = i
print(max_s)
