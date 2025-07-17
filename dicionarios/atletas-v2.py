import requests, json

try:
    dados = requests.get("https://api.cartola.globo.com/atletas/mercado").text
    dados = json.loads(dados)
    atletas = dados["atletas"]
    posicoes = dados["posicoes"]
    
    flamengo = []
    for atleta in atletas:
        nome_posicao = posicoes[str(atleta["posicao_id"])]["nome"]
        if atleta["clube_id"] == 262:  # Flamengo/RJ
            flamengo.append([atleta["nome"], atleta["apelido"], nome_posicao, atleta["posicao_id"], atleta["preco_num"]])
    
    flamengo.sort(key=lambda x: x[4], reverse=True)  # Ordena por posição_id em ordem decrescente
    for atleta in flamengo:
        print(f"{atleta[1]} -> {atleta[0]} | Posição: {atleta[2]} ({atleta[3]}) | Preço: C${atleta[4]:.2f}")
except json.decoder.JSONDecodeError as e:
    print ("Erro na conversão de JSON para dicionario")