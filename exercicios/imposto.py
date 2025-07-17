#entrada - salário bruto.

#processamento - cálculo do imposto a ser cobrado.

#saida - salário líquido (bruto - imposto) e o imposto.

print("Cálculo de imposto de renda")

salariobruto = float(input("Insira o seu salário bruto: "))
minimoimposto = 2428.80


if salariobruto > 4664.68:
    imposto = (salariobruto * 0.275) - 908.73
else:
    if 3751.06 < salariobruto < 4664.68:
        imposto = (salariobruto * 0.225) - 675.49
    else:
        if 2826.66 < salariobruto < 3751.05:
            imposto = (salariobruto * 0.15) - 394.16
        else:
            if 2428.81 < salariobruto < 2826.65:
                imposto = (salariobruto * 0.075) - 182.16                
            else:
                imposto = 0
                print("Você istá isento de impostos.")

liquido = salariobruto - imposto
print("Você vai pagar ", imposto, " reais de imposto. Seu salário líquido vai ser: ", liquido, " reais.")