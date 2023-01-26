n = int(input())
l = sorted(list(map(int, input().split())))

print(f"{max(l) - min(l)}")
