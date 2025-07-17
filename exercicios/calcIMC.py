print("Cálculo de IMC")

peso = float(input("Insira o seu peso: "))
altura = float(input("Insira sua altura: "))
imc = round(peso / (altura ** 2))


if imc < 18.5:
    classificacao = "Magreza"
    obesidade = 0
else:
    if 18.5 < imc < 24.9:
        classificacao = "Normal"
        obesidade = 0
    else:
        if 25 < imc < 29.9:
            classificacao = "Sobrepeso"
            obesidade = 1
        else:
            if 30 < imc < 39.9:
                classificacao = "Obesidade"
                obesidade = 2               
            else:
                if imc >= 40:
                    classificacao = "Obesidade grave"
                    obesidade = 3

print("Seu IMC é :", imc)
print("Classificação: ", classificacao)
print("Grau de obesidade: ", obesidade)

                    