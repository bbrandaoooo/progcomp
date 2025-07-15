import requests, json

try:
    dados = requests.get("https://api.cartola.globo.com/atletas/mercado").text
    dados = json.loads(dados)
    atletas = dados["atletas"]
    posicoes = dados["posicoes"]
    clubes = dados["clubes"]

    nome_clube = input("Digite o nome do clube: ").upper()
    for clube in clubes.values():
        if nome_clube == clube["nome_fantasia"].upper():
            clube_id: clube["id"]
            print(f"Identificado {nome_clube} -> {clube_id}")
            break
    
    equipe = []
    for atleta in atletas:
        nome_posicao = posicoes[str(atleta["posicao_id"])]["nome"]
        if atleta["clube_id"] == clube_id:
            equipe.append([atleta["nome"], atleta["apelido"], nome_posicao, atleta["posicao_id"], atleta["preco_num"]])
    
    equipe.sort(key=lambda x: x[4], reverse=True)  # Ordena por posição_id em ordem decrescente
    for atleta in equipe:
        print(f"{atleta[1]} -> {atleta[0]} | Posição: {atleta[2]} ({atleta[3]}) | Preço: C${atleta[4]:.2f}")
    else:
        print('Clube não encontrado.')
except json.decoder.JSONDecodeError as e:
    print ("Erro na conversão de JSON para dicionario")