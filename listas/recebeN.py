import random

n = int(input("Digite um número: "))
lista = []

for i in range(100):
    lista.append(random.randint(-n, n))

print(list(filter(lambda x: (x % 2 == 0) and (x >= 0), lista)))

# O código recebe um número inteiro do usuário, gera uma lista de 100 números aleatórios entre -n e n,
# e imprime os números pares e não negativos dessa lista.