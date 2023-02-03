total = sum(map(int, input()))

pinyin = ["ling", "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu"]
l = []
for i in str(total):
    l.append(pinyin[int(i)])
print(" ".join(l))
