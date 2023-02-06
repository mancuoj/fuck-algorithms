while True:
    s = input()
    if s == ".":
        break

    for i in range(1, len(s) + 1):
        if len(s) % i == 0:
            ss = ""
            cnt = len(s) // i
            for j in range(cnt):
                ss += s[:i]
            if ss == s:
                print(cnt)
                break
