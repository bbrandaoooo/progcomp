maiorcomb = 0
maiorp = 0
for p in range(1, 500):
    solucao = 0
    for a in range(1, p // 3 + 1):
        for b in range(a, p + 1 - a):
            c = p - (a+b)
            if c > 0:
                a2 = a*a
                b2 = b*b
                c2 = c*c
                if (a2+b2) == c2:
                    print("para ", p, "=", a, b, c)
                    solucao += 1
                elif (a2 + b2) > c2:
                    break
    if solucao > maiorcomb:
        maiorcomb = solucao
        maiorp = p
print(maiorcomb)