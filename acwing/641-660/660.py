x, y = map(int, input().split())  # split 不加参数默认空格

prices = [0, 4, 4.5, 5, 2, 1.5]
print(f"Total: R$ {prices[x] * y:.2f}")

# print("Total: R$ %.2lf" % (prices[x] * y))
