list = [int(input()) for _ in range(10)]
for i in range(10):
    print(f"X[{i}] = {list[i] if list[i] > 0 else 1}")
