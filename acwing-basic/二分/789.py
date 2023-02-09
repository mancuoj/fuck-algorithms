n, q = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(q):
    x = int(input())

    l, r = 0, n - 1
    while l < r:
        mid = (l + r) // 2
        if a[mid] >= x:
            r = mid
        else:
            l = mid + 1

    if a[l] != x:
        print("-1 -1")
    else:
        print(l, end=" ")
        l, r = 0, n - 1
        while l < r:
            # 避免 r = l + 1 时 (l + r) ÷ 2 = l 陷入死循环
            mid = (l + r + 1) // 2
            if a[mid] <= x:
                l = mid
            else:
                r = mid - 1
        print(r)
