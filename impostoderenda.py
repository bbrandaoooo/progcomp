print("Cálculo de Imposto de Renda")

bruto = float(input("Digite o seu salário bruto: "))


if bruto > 4664.68:
    imposto = (bruto * 0.275) - 908.73
else:
    if 3751.06 < bruto < 4664.68:
        imposto = (bruto * 0.225) - 675.49
    else:
        if 2826.66 < bruto < 3751.05:
            imposto = (bruto * 0.15) - 394.16
        else:
            if 2428.81 < bruto < 2826.65:
                imposto = (bruto * 0.075) - 182.16
            else:
                print("Você está isento de impostos.")




liquido = bruto - imposto
print("Você precisa pagar imposto. Seu salário líquido é de :", liquido)