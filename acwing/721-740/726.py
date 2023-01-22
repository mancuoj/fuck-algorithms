import math

n = int(input())

for _ in range(n):
    x = int(input())
    flag = True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            print(x, "is not prime")
            break
    else:  # for 循环正常结束时执行
        print(x, "is prime")
