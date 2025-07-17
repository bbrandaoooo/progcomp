print("Fatorial de um número")

n = int(input("Insira um número: "))
contador = 1
resultado = 1

while contador <= n:
    resultado = resultado * contador
    contador = contador + 1
    print(resultado)