from math import sqrt


def is_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


l = int(input())

total, cnt = 0, 0
for i in range(2, 100010):
    if is_prime(i):
        if total + i > l:
            print(cnt)
            break
        print(i)
        total += i
        cnt += 1
