n = int(input())
x = list(map(int, input().split()))

min, min_index = x[0], 0
for i in range(1, n):
    if x[i] < min:
        min = x[i]
        min_index = i

print(f"Minimum value: {min}")
print(f"Position: {min_index}")
