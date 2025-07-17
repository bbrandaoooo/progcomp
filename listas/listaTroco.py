produtos = ['Hamburguer', 'Pizza', 'Refrigerante', 'Batata Frita', 'Salada', 'Suco Natural', 'Sorvete']
preco = [15.00, 30.00, 5.00, 10.00, 12.00, 8.00, 7.00]
cedulas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00]

# Escolhe o produto, insere o valor pago e retorna o troco:

for pos in range(len(produtos)):
    print(produtos[pos], preco[pos])

produtoEscolhido = int(input('Escolha um produto de 0 a 6: '))
valorPago = int(input('Quanto você pagou? '))
troco = valorPago - preco[produtoEscolhido]
print(f'Seu troco é de R${troco:.2f}')

# Retorna quantas cédulas de cada valor teve no troco:

restante = troco
for cedula in cedulas:
    quantidade = int(restante // cedula)
    if quantidade > 0:
        print(f'{quantidade} cédula(s) de R${cedula:.2f}')
        restante -= quantidade * cedula
    