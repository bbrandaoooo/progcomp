import requests, json

try:
    dados = requests.get("https://api.cartola.globo.com/atletas/mercado").text
    atletas = json.loads(dados)["atletas"]
    
    '''   for atleta in atletas:
        if atleta["clube_id"] == 263: # Botafogo/RJ
            print (f"{atleta['apelido']} -> {atleta['nome']}")
    '''
    
    # Mapeamento de posições:
    posicoes = {
        1: "Goleiro",
        2: "Lateral",
        3: "Zagueiro",
        4: "Meia",
        5: "Atacante",
        6: "Técnico"
    }
    
    botafogo = filter (lambda x: x['clube_id'] == 263, atletas)
    for atleta in botafogo:
        posicao_id = atleta['posicao_id']
        posicao_nome = posicoes.get(posicao_id, 'Desconhecida')
        print('\n')
        print (f"{atleta['apelido']} -> {atleta['nome']} | Posição: {posicao_nome} ({posicao_id})")
except json.decoder.JSONDecodeError as e:
    print ("Erro na conversão de JSON para dicionario")