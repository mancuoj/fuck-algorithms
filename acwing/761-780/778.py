s, s1, s2 = input().split(",")

if s1 in s and s2 in s:
    cnt = s.rfind(s2) - s.find(s1) - len(s1)
    if cnt >= 0:
        print(cnt)
    else:
        print(-1)
else:
    print(-1)
