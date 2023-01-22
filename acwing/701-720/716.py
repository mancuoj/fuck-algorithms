max, max_index = 0, 1

for i in range(100):
    x = int(input())
    if x > max:
        max = x
        max_index = i + 1

print(max)
print(max_index)
