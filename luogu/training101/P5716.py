y, m = map(int, input().split())

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    days[2] = 29
print(days[m])
