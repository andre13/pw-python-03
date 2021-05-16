import sys

def calcula_linhas (nomeFicheiro):
    nrLinhas = 0
    try:
        with open(nomeFicheiro, encoding='utf-8') as f:
            conteudo = f.readlines()
    except OSError:
        print("Não foi possível aceder ao ficheiro.")
        sys.exit()
    
    return sum(1 for linha in conteudo)


def calcula_carateres  (nomeFicheiro):
    nrCaracteres = 0
    try:
        with open(nomeFicheiro, encoding='utf-8') as f:
            conteudo = f.readlines()
    except OSError:
        print("Não foi possível aceder ao ficheiro.")
        sys.exit()

    for linha in conteudo:
        nrCaracteres += len(linha)

    return nrCaracteres


def calcula_palavra_comprida (nomeFicheiro):
    try:
        with open(nomeFicheiro, encoding='utf-8') as f:
            conteudo = f.read().split()
            conteudo = [palavra.replace(',','') for palavra in conteudo]
    except OSError:
        print("Não foi possível aceder ao ficheiro.")
        sys.exit()

    return max(conteudo, key=len)


def calcula_ocorrencia_de_letras (nomeFicheiro):
    dicionarioLetras = {}
    try:
        with open(nomeFicheiro, encoding='utf-8') as f:
            conteudo = f.read()
            letras = [caracter for caracter in conteudo.lower() if caracter.isalpha()]

            for letra in set(letras):
                contador = letras.count(letra)
                dicionarioLetras[letra] = contador
    except OSError:
        print("Não foi possível aceder ao ficheiro.")
        sys.exit()

    return dicionarioLetras