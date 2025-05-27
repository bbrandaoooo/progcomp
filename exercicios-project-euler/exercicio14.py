print("Sequência de Collatz")

n = int(input("Digite o número que você deseja saber a sequência de Collatz: "))

while n > 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (3 * n) + 1
    print(n)