max = 8
max_index = 0
for i in range(1, 8):
    a, b = map(int, input().split())
    if a + b > max:
        max = a + b
        max_index = i
print(max_index)
