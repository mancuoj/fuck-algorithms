sign = input()

sum, cnt = 0, 0
for i in range(12):
    arr = list(map(float, input().split()))
    for j in range(12):
        if j > i:
            sum += arr[j]
            cnt += 1

if sign == "M":
    sum /= cnt

print(f"{sum:.1f}")
