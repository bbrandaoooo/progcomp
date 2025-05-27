print("Programa que diz o maior fator primo de um número.")

numero = int(input("Insira um número para descobrir o maior fator primo dele: "))
x = 2

while numero > 1:
    if numero % x == 0:
        numero = numero // x
    else:
        x += 1

print(f"O maior fator desse número é: {x}")