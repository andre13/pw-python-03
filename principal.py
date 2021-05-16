import analisa_ficheiro.acessorio as acessorio
import analisa_ficheiro.calculos as calculos
import json

def main():
    nomeFicheiro = acessorio.pede_nome()
    ficheiroJson = acessorio.gera_nome (nomeFicheiro)
    nLinhas = str(calculos.calcula_linhas(nomeFicheiro))
    nCarateres = str(calculos.calcula_carateres(nomeFicheiro))
    palavraComprida = str(calculos.calcula_palavra_comprida(nomeFicheiro))
    ocorrenciasLetras = [calculos.calcula_ocorrencia_de_letras(nomeFicheiro)]
    with open(ficheiroJson, 'w', encoding='utf8') as json_file:
        dic_calculos = {'Números de linhas':nLinhas,
                        'Número de caractéres': nCarateres,
                        'Palavra mais comprida': palavraComprida,
                        'Ocorrências de letras': ocorrenciasLetras
        }
        json.dump(dic_calculos, json_file, indent = 4, ensure_ascii=False)
        print(f"Os resultados foram guardados no ficheiro `historia.json`")

if __name__ == "__main__": 
    main()