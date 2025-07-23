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
    print(max (logsMinuto.values()))
except FileNotFoundError as e:
    print(f"O arquivo {nomeArquivo} não está acessível")
    exit()