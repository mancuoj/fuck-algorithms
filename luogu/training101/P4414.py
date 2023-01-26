l = sorted(list(map(int, input().split())))
s = input()

for i in range(3):
    print(l[ord(s[i]) - 65], end=" ")
