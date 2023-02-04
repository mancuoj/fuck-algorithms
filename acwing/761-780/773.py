import sys

for line in sys.stdin:
    s, subs = line.split()
    max_s, max_index = s[0], 0
    for i in range(1, len(s)):
        if s[i] > max_s:
            max_s = s[i]
            max_index = i
    print(s[: max_index + 1] + subs + s[max_index + 1 :])
