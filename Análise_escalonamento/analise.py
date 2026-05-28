import math

def estatisticas(vetor):
    n = len(vetor)

    media = sum(vetor) / n

    vetor_ordenado = sorted(vetor)

    if n % 2 == 0:
        mediana = (vetor_ordenado[n // 2 - 1] + vetor_ordenado[n // 2]) / 2
    else:
        mediana = vetor_ordenado[n // 2]

    soma = 0
    for valor in vetor:
        soma += (valor - media) ** 2

    variancia = soma / n
    desvio_padrao = math.sqrt(variancia)

    minimo = min(vetor)
    maximo = max(vetor)

    return {
        "média": media,
        "mediana": mediana,
        "desvio_padrão": desvio_padrao,
        "mínimo": minimo,
        "máximo": maximo
    }


arquivos = [
    "resultados_01FCFS.txt",
    "resultados_02FCFS.txt",
    "resultados_03FCFS.txt",
    "resultados_04FCFS.txt",

    "resultados_01EG.txt",
    "resultados_02EG.txt",
    "resultados_03EG.txt",
    "resultados_04EG.txt",

    "resultados_01SPN.txt",
    "resultados_02SPN.txt",
    "resultados_03SPN.txt",
    "resultados_04SPN.txt"
]


for arquivo in arquivos:

    cpu_tempos = []
    io_tempos = []

    with open(arquivo, "r") as f:

        for linha in f:

            partes = linha.split()

            if len(partes) != 3:
                continue

            tipo, pid, tempo = partes

            tempo = float(tempo)

            if tipo == "CPU":
                cpu_tempos.append(tempo)

            elif tipo == "IO":
                io_tempos.append(tempo)

    print("\nArquivo:", arquivo)
    print("CPU:", cpu_tempos)
    print("IO:", io_tempos)

    print("\n========================")
    print(f"Arquivo: {arquivo}")

    print("\nCPU")
    resultado_cpu = estatisticas(cpu_tempos)

    for chave, valor in resultado_cpu.items():
        print(f"{chave}: {valor}")

    print("\nIO")
    resultado_io = estatisticas(io_tempos)

    for chave, valor in resultado_io.items():
        print(f"{chave}: {valor}")