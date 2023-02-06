s1, s2 = input().split()

if len(s1) > len(s2):
    s1, s2 = s2, s1

s2 += s2
if s1 in s2:
    print("true")
else:
    print("false")
