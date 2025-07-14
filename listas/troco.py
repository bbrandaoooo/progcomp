# lista para os produtos
# lista pro preço do produto
# lista da quantidade de cédulas para o troco

produtos = ['laranja', 'maçã', 'goiaba', 'uva', 'banana']
precoProd = [2, 1.50, 3, 4, 5]

for pos in range(len(produtos)):
    print(produtos[pos], precoProd[pos])
produtoEscolhido = int(input('Escolha um produto de 0 a 4: '))
produtoEscolhido += [] 