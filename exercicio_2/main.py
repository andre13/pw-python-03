import csv
import analise_pasta as funcoes


ficheiro_resultados = funcoes.guarda_resultados(funcoes.faz_calculos(funcoes.pede_pasta()))

with open(ficheiro_resultados, 'r') as f:
    nrLinha = 0
    lista_chaves, lista_volumes, lista_quantidades = ([] for l in range(3))
    for linha in csv.reader(f):
        nrLinha += 1
        if nrLinha != 1:
            lista_chaves.append(linha[0])
            lista_quantidades.append(linha[1])
            lista_volumes.append(linha[2])

titulo = 'Programação Web'
funcoes.faz_grafico_queijos(titulo, lista_chaves, lista_quantidades)
funcoes.faz_grafico_barras(titulo, lista_chaves, lista_volumes)