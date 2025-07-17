fd = open ("dados2.txt", "w")
dados = "Este conteudo foi criado por um \n"
dados += "programa em python\n"
fd.write(dados)
fd.close()