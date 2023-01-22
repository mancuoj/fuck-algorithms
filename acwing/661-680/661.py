a, b, c, d = map(float, input().split())

x = a * 0.2 + b * 0.3 + c * 0.4 + d * 0.1
print(f"Media: {x:.1f}")

if x >= 7:
    print("Aluno aprovado.")
elif x >= 5:
    print("Aluno em exame.")
    y = float(input())
    print(f"Nota do exame: {y:.1f}")
    z = (x + y) / 2
    if z >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {z:.1f}")
else:
    print("Aluno reprovado.")
