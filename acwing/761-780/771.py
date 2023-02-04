n = int(input())

for _ in range(n):
    s = input()
    max_n, max_s = 0, ""
    for i in range(len(s)):
        j, cnt = i, 0
        while j < len(s) and s[i] == s[j]:
            j += 1
            cnt += 1
        if cnt > max_n:
            max_n = cnt
            max_s = s[i]
        i = j - 1
    print(max_s, max_n)
