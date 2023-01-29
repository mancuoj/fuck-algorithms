n = input()

s = 0
pinyin = ["ling", "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu"]
for i in range(len(n)):
    s += int(n[i])

s = str(s)
for i in range(len(s) - 1):
    print(pinyin[int(s[i])], end=" ")
print(pinyin[int(s[len(s) - 1])])
