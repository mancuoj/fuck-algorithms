n = int(input())
l = sorted(list(map(int, input().split())))

print(f"{(sum(l) - l[0] - l[n-1]) / (n - 2):.2f}")
