import os

def pede_nome ():
    while True:
        nomeFicheiro = input("Introduza o nome do ficheiro (.txt): ")
        if nomeFicheiro.endswith(".txt"):
            ficheiro = os.path.join(os.getcwd(), nomeFicheiro)
            if os.path.isfile(ficheiro):
                break
            else:
                print("Ficheiro não existe.")
        else:
            print("Nome inválido ou Extensão inválida, tente novamente.")

    return nomeFicheiro


def gera_nome (nome):
    nomeJson = os.path.splitext(nome)[0]+".json"
    return nomeJson