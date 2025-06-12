#Questão 2

n = int(input('Digite o número que você quer o fatorial: '))
m = int(input('Digite o número que você deseja dividir o fatorial: '))

resultado = 1
contador = 1

while contador <= n:
    resultado *= contador
    contador += 1
    print(resultado)
for i in range(n + 1, m):
    if contador % i == 0:
        print(i, ' é um Jaime de ', n)
