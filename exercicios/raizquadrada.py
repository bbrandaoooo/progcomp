print("Calculadora de Raizes de uma Equação de Segundo Grau")

a = int(input("Informe o valor de A = "))
b = int(input("Informe o valor de B = "))
c = int(input("Informe o valor de C = "))

delta = b**2-4*a*c
print ("Valor de Delta = ", delta)

x1 = ((-b) + (delta ** (1/2))) / (2 * a)
x2 = ((-b) - (delta ** (1/2))) / (2 * a)

print("As raizes da Equação de Segundo Grau são: ", x1, " e ", x2)