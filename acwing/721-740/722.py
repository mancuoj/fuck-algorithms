while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break
    if m > n:
        m, n = n, m

    total = 0
    for i in range(m, n + 1):
        print(i, end=" ")
        total += i
    print(f"total={total}")
