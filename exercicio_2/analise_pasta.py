import os
import csv
from matplotlib import pyplot as plt
from os.path import dirname

def obtem_tipos_fichs (diretorio):
    return [os.path.splitext(ficheiro)[1] for ficheiro in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, ficheiro))]

def pede_pasta ():
    caminho = input("Caminho da pasta: ")
    if not os.path.isdir(caminho):
        print("Caminho de pasta inválido")
        caminho = None
    
    return caminho

def faz_calculos (diretorio):
    dic_info = {}
    ficheiros = [ficheiro for ficheiro in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, ficheiro))]
    extensoes = obtem_tipos_fichs(diretorio)

    for extensao in set(extensoes):
        volume = sum(os.path.getsize(os.path.join(diretorio, ficheiro)) for ficheiro in ficheiros if ficheiro.endswith(extensao))
        quantidade = extensoes.count(extensao)
        dic_info[extensao] = {"volume":volume/2**10 , "quantidade":quantidade}

    return dic_info

def guarda_resultados (dic_resultados):
    ficheiro = os.path.join(os.getcwd(), 'resultados.csv')
    with open(ficheiro, 'w', newline='') as f:
        campos = ['Extensao', 'Quantidade', 'Tamanho[kByte]']
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for extensao, medidas in dic_resultados.items():
            writer.writerow({'Extensao':extensao, 'Quantidade':medidas['quantidade'], 'Tamanho[kByte]':medidas['volume']})

    print(f"{ficheiro}")

    return ficheiro

def faz_grafico_queijos(titulo, lista_chaves, lista_valores):
    
    plt.pie(lista_valores, labels=lista_chaves, autopct='%1.0f%%')
    plt.title(titulo)
    plt.show()
    
def faz_grafico_barras(titulo, lista_chaves, lista_valores):
    
    plt.bar(lista_chaves, lista_valores)
    plt.title(titulo)
    plt.show()