print("Capital aplicado ao mês")

c = int(input("Insira o seu capital: "))
d = int(input("De quanto serão os seus depósitos mensais? "))
i = int(input("De quanto será a taxa de juros mensal? "))
n = int(input("Em quantos meses? "))

saldo = round(c * (1+i/100) ** n + d * ((1+i/100) ** n - (1+i/100)) / (i/100))

print("O seu saldo será de ", saldo, " reais")