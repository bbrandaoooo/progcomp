import sys

nomeArquivo = "apache.logs"
try:
    fdLogs = open (nomeArquivo, "r")
    logsMinuto = {}
    for log in fdLogs:
        inicioTempo = log.find('[')
        fimTempo = log.find(']')
        tempo = log[inicioTempo+1:fimTempo][:17]
        if tempo in logsMinuto:
            logsMinuto[tempo] += 1
        else:
            logsMinuto[tempo] = 1
    fdLogs.close()
    maisOcorre = (max (logsMinuto.items(), key=lambda item: item[1]))
    print(f"A data com mais acessos é {maisOcorre[0]} com {maisOcorre[1]} acessos.")
except FileNotFoundError as e:
    print(f"O arquivo {nomeArquivo} não está acessível")
    exit()