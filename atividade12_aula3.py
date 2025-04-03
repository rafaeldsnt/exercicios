class Conta:
    def __init__(self, num_conta, nome_titular, saldo, limite):
        self.num_conta = num_conta
        self.nome_titular = nome_titular
        self.saldo = saldo
        self.limite = limite
    
    def Depositar(self, num_conta, saldo, valor):
        print(f"O valor inicial é {self.saldo}")
        self.saldo = self.saldo + valor
        print(f"O valor final é {self.saldo}")
        

    def Sacar(self, num_conta, saldo, valor ):

        if (self.limite + self.saldo >  - valor):
            print(f"Você não poderá efetuar esse Saque. Pois o mesmo ultrapassa o seu limite. O limite disponibilizado é de {(self.limite + self.saldo)}")
        else:
            print(f"O valor inicial é {self.saldo}")
            self.saldo = self.saldo - valor
            print(f"O valor final é {self.saldo}")
        

    def exibir_info(self):
        print(f"O nome titular da conta {self.nome_titular} o numero da conta {self.num_conta}  e o seu saldo é {self.saldo}"  )


class Banco:
      def __init__(self):
         self.contas = {}


if __name__ == "__main__":
    cc_1= Conta("001","Rafael", 0, 1000); 
    
    valor_deposito = float(input("Informe o valor que será depositado:"))
    cc_1.Depositar("", "", valor_deposito)


    valor_saque = float(input("Informe o valor que será sacado:"))
    cc_1.Sacar("", "", valor_saque)

    cc_1.exibir_info()