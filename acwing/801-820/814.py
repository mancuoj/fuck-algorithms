*_, size = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in a[:size] + b[size:]:
    print(i, end=" ")
