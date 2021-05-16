import sys

class DepositoInsufException(Exception):
    pass

class CombustivelInsufException(Exception):
    pass

class automovel ():
    def __init__(self, cap_dep, quant_comb, consumo):
        self.cap_dep = cap_dep
        self.quant_comb = quant_comb
        self.consumo = consumo
    
    def combustivel (self):
        return self.quant_comb

    def autonomia (self):
        return int((self.quant_comb / self.consumo) * 100)

    def abastece(self, n_litros):
        try:
            if (self.quant_comb + n_litros) > self.cap_dep:
                raise DepositoInsufException()
            else:
                self.quant_comb += n_litros
        except (DepositoInsufException):
            print(f"O carro tem {self.quant_comb} litros. A adição de {n_litros} litros excede a capacidade de {self.cap_dep} litros do depósito")

        return self.autonomia()

    def percorre(self, n_km):
        try:
            if n_km > self.autonomia():
                raise CombustivelInsufException()
            else:
                self.quant_comb -= (n_km * self.consumo) / 100
        except (CombustivelInsufException):
            print(f"O carro não tem autonomia suficiente para fazer {n_km} Km.")

        return self.autonomia()

def imprime_menu ():
    print("Gerir Automóvel:")
    print("  1 - Combustível no depósito")
    print("  2 - Autonomia")
    print("  3 - Abastecer automóvel")
    print("  4 - Fazer viagem")
    print(" -1  - Terminar o programa")

def recebe_opcao ():
    while True:
        lista_opcoes = ['1', '2', '3', '4', '-1']
        opcao = input("Introduza a opção: ")
        if opcao in lista_opcoes:
            break
        else:
            print("Opção inválida.")
    
    return opcao

def obter_quantidade ():
    while True:
        try:
            quantidade = float(input("Introduza a quantidade: "))
            break
        except:
            print("Só são permitidos números.")
    
    return quantidade

def main ():
    a1 = automovel(60, 10, 15)
    
    while True:
        print("\n")
        imprime_menu()
        opcao = recebe_opcao()
        if opcao == '1':
            print(f"> {a1.combustivel()} litros no depósito")
        elif opcao == '2':
            print(f"> {a1.autonomia()} Km de autonomia")
        elif opcao == '3':
            print(f"> Autonomia: {a1.abastece(obter_quantidade())}")
        elif opcao == '4':
            print(f"> Autonomia: {a1.percorre(obter_quantidade())}")
        elif opcao == '-1':
            break
    
    print("Programa terminado.")
    sys.exit()




if __name__ == "__main__": 
  main()