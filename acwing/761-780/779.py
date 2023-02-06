while True:
    n = int(input())
    if n == 0:
        break

    min_ = 210
    s = input()
    for _ in range(1, n):
        ss = input()
        ans, i = 0, 0
        while i < len(s) and i < len(ss):
            if s[len(s) - 1 - i] == ss[len(ss) - 1 - i]:
                ans += 1
            else:
                break
            i += 1
        min_ = min(ans, min_)

    if min_:
        print(s[-min_:])
    else:
        print()
