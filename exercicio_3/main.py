import os
from os.path import abspath

def pede_caminho ():
    while True:
        pasta = input("Introduza o caminho (relativo ou absoluto) da pasta: ")
        if os.path.isdir(pasta):
            break
        else:
            print("A pasta não existe.")
            
    return pasta

def calcula_tamanho_pasta(pasta):
    soma = 0
    for elemento in os.listdir(pasta):
        diretorio_elemento = os.path.join(pasta, elemento)
        if os.path.isfile(diretorio_elemento):
            soma += os.path.getsize(diretorio_elemento)/2**20 #conversão para MBytes a cada ficheiro lido
        elif os.path.isdir:
            soma += calcula_tamanho_pasta(diretorio_elemento)
    
    return soma 

def main ():
    pasta = pede_caminho()
    tamanho = calcula_tamanho_pasta(os.path.abspath(pasta)) #envia como parametro o path absoluto
    print(f"O tamanho total do diretorio é: {tamanho}")


if __name__ == "__main__": 
  main()