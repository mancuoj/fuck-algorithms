a, b, c = sorted(map(int, input().split()))

if a + b <= c:
    print("Not triangle")
else:
    if a * a + b * b > c * c:
        print("Acute triangle")
    elif a * a + b * b == c * c:
        print("Right triangle")
    else:
        print("Obtuse triangle")

    if a == b or b == c or a == c:
        print("Isosceles triangle")

    if a == b == c:
        print("Equilateral triangle")
