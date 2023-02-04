n = int(input())
l = sorted(map(int, input().split()))

print(f"{max(l) - min(l)}")
