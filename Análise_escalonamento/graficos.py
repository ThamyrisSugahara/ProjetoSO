import math
import matplotlib.pyplot as plt
import numpy as np


# Função para calcular estatísticas

def estatisticas(vetor):

    n = len(vetor)

    media = sum(vetor) / n

    vetor_ordenado = sorted(vetor)

    if n % 2 == 0:
        mediana = (
            vetor_ordenado[n // 2 - 1]
            + vetor_ordenado[n // 2]
        ) / 2
    else:
        mediana = vetor_ordenado[n // 2]

    soma = 0

    for valor in vetor:
        soma += (valor - media) ** 2

    variancia = soma / n

    desvio_padrao = math.sqrt(variancia)

    return {
        "media": media,
        "mediana": mediana,
        "maximo": max(vetor),
        "desvio_padrao": desvio_padrao
    }


# Arquivos dos algoritmos

algoritmos = {

    "Padrão": [
        "resultados_01PADRAO.txt",
        "resultados_02PADRAO.txt",
        "resultados_03PADRAO.txt",
        "resultados_04PADRAO.txt"
    ],

    "FCFS": [
        "resultados_01FCFS.txt",
        "resultados_02FCFS.txt",
        "resultados_03FCFS.txt",
        "resultados_04FCFS.txt"
    ],

    "EG": [
        "resultados_01EG.txt",
        "resultados_02EG.txt",
        "resultados_03EG.txt",
        "resultados_04EG.txt"
    ],

    "SPN": [
        "resultados_01SPN.txt",
        "resultados_02SPN.txt",
        "resultados_03SPN.txt",
        "resultados_04SPN.txt"
    ]
}


# Cenários (número de processos)

cenarios = [10, 50, 100, 200]

# Dicionários de dados

dados_cpu_media = {}
dados_cpu_mediana = {}
dados_cpu_maximo = {}
dados_cpu_desvio = {}

dados_io_media = {}
dados_io_mediana = {}
dados_io_maximo = {}
dados_io_desvio = {}

# Leitura dos arquivos

for nome_algoritmo, arquivos in algoritmos.items():

    medias_cpu = []
    medianas_cpu = []
    maximos_cpu = []
    desvios_cpu = []


    medias_io = []
    medianas_io = []
    maximos_io = []
    desvios_io = []

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

        est_cpu = estatisticas(cpu_tempos)
        est_io = estatisticas(io_tempos)

        medias_cpu.append(est_cpu["media"])
        medianas_cpu.append(est_cpu["mediana"])
        maximos_cpu.append(est_cpu["maximo"])
        desvios_cpu.append(est_cpu["desvio_padrao"])

        medias_io.append(est_io["media"])
        medianas_io.append(est_io["mediana"])
        maximos_io.append(est_io["maximo"])
        desvios_io.append(est_io["desvio_padrao"])

    dados_cpu_media[nome_algoritmo] = medias_cpu
    dados_cpu_mediana[nome_algoritmo] = medianas_cpu
    dados_cpu_maximo[nome_algoritmo] = maximos_cpu
    dados_cpu_desvio[nome_algoritmo] = desvios_cpu

    dados_io_media[nome_algoritmo] = medias_io
    dados_io_mediana[nome_algoritmo] = medianas_io
    dados_io_maximo[nome_algoritmo] = maximos_io
    dados_io_desvio[nome_algoritmo] = desvios_io


# Funcao para plotar gráficos

def plotar_grafico_geral(titulo, dados_cpu, dados_io):

    plt.figure(figsize=(10,5))

    for algoritmo in dados_cpu.keys():

        plt.plot(
            cenarios,
            dados_cpu[algoritmo],
            marker="o",
            linestyle="-",
            label=f"{algoritmo} CPU"
        )

        plt.plot(
            cenarios,
            dados_io[algoritmo],
            marker="s",
            linestyle="--",
            label=f"{algoritmo} IO"
        )

    plt.title(titulo)
    plt.xlabel("Nº de processos")
    plt.ylabel("Tempo médio (s)")
    plt.xticks(cenarios)
    plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left")

    plt.tight_layout()
    plt.show()

def plotar_grafico(titulo, ylabel, dados, limite_y=None):

    x = np.arange(len(cenarios))
    nomes_algoritmos = list(dados.keys())
    largura = 0.8 / len(nomes_algoritmos)

    fig, ax = plt.subplots(figsize=(10,5))

    for i, algoritmo in enumerate(nomes_algoritmos):
        deslocamento = (i - len(nomes_algoritmos) / 2) * largura + largura / 2

        ax.bar(
            x + deslocamento,
            dados[algoritmo],
            largura,
            label=algoritmo
        )

    if limite_y is not None:
        ax.set_ylim(limite_y)
    else:
        maior_valor = max(max(v) for v in dados.values())
        ax.set_ylim(0, maior_valor * 1.1)

    ax.set_title(titulo)
    ax.set_xlabel("Número de processos")
    ax.set_ylabel(ylabel)
    ax.set_xticks(x)
    ax.set_xticklabels(cenarios)
    ax.legend()

    plt.tight_layout()
    plt.show()

# Gráficos CPU

plotar_grafico(
    "CPU-bound (Média)",
    "Tempo médio CPU (s)",
    dados_cpu_media,
    limite_y=(0, 0.13)

)

plotar_grafico(
    "CPU-bound (Mediana)",
    "Tempo mediano CPU (s)",
    dados_cpu_mediana,
    limite_y=(0, 0.13)
)

plotar_grafico(
    "CPU-bound (Máximo)",
    "Tempo máximo CPU (s)",
    dados_cpu_maximo,
    limite_y=(0, 0.13)
)

plotar_grafico(
    "CPU-bound (Desvio Padrão)",
    "Desvio padrão CPU",
    dados_cpu_desvio,
    limite_y=(0, 0.05)
)

# GráficosIO

plotar_grafico(
    "IO-bound (Média)",
    "Tempo médio IO (s)",
    dados_io_media
)

plotar_grafico(
    "IO-bound (Mediana)",
    "Tempo mediano IO (s)",
    dados_io_mediana
)

plotar_grafico(
    "IO-bound (Máximo)",
    "Tempo máximo IO (s)",
    dados_io_maximo
)

plotar_grafico(
    "IO-bound (Desvio Padrão)",
    "Desvio padrão IO",
    dados_io_desvio
)

#Gráficos de comparação geral

plotar_grafico_geral(
    "Comparação Geral (CPU e IO) - Média",
    dados_cpu_media,
    dados_io_media
)

plotar_grafico_geral(
    "Comparação Geral (CPU e IO) - Mediana",
    dados_cpu_mediana,
    dados_io_mediana
)

plotar_grafico_geral(
    "Comparação Geral (CPU e IO) - Máximo",
    dados_cpu_maximo,
    dados_io_maximo
)

plotar_grafico_geral(
    "Comparação Geral (Desvio Padrão)",
    dados_cpu_desvio,
    dados_io_desvio
)