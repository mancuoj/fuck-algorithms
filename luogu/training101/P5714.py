m, h = map(float, input().split())

bmi = m / h / h
if bmi < 18.5:
    print("Underweight")
elif bmi < 24:
    print("Normal")
else:
    print(f"{bmi:.6g}")
    print("Overweight")
