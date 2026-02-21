# Objetivo: praticar POO avançada com ContaBancaria
# Exercício: usar property, setter com validação, dunder __add__, __str__, __repr__

class ContaBancaria:
    # Quando eu crio a conta nova, isso roda primeiro
    def __init__(self, titular, saldo_inicial=500):
        # titular é o nome da pessoa que tem a conta
        self._titular = titular
        # _saldo é onde fica o dinheiro de verdade
        # coloquei underline pra lembrar que não devo mudar direto | tem que usar os métodos
        self._saldo = saldo_inicial     # começa com 500 se eu não passar valor

    # Isso aqui deixa eu pegar o nome fácil: print(conta.titular)
    @property                       # o @property transforma isso em algo que parece atributo normal
    def titular(self):
        # só devolvo o nome que guardei lá em cima
        return self._titular

    # Mesma coisa pro saldo: deixa ver bonito com R$
    @property
    def saldo(self):
        # formato com R$ e duas casas (ex: R$ 123.45)
        # uso o _saldo real pra calcular isso
        return f"R$ {self._saldo:.2f}"

    # Quando alguém tenta mudar o saldo direto (conta.saldo = 100)
    @saldo.setter                   # o setter roda nessa hora
    def saldo(self, valor):
        # verifico se o valor novo é negativo
        if valor < 0:
            # se for negativo jogo o erro pra não deixar acontecer
            # assim o programa para e avisa
            raise ValueError("Não pode colocar saldo negativo!")
        # se for ok 0 > mudo o valor real
        self._saldo = valor

    # Função pra colocar dinheiro na conta
    def depositar(self, valor):
        # só aceito se o valor for maior que zero
        if valor > 0:
            # somo no saldo escondido
            self._saldo += valor
            # mostro mensagem pra saber que deu certo
            print(f"Depósito de R${valor:.2f} feito com sucesso.")
        else:
            # aviso se tentar depositar negativo ou zero
            print("Valor de depósito deve ser positivo.")

    # Função pra tirar dinheiro
    def sacar(self, valor):
        # primeiro vejo se o valor é positivo
        if valor > 0:
            # depois vejo se tem dinheiro suficiente na conta
            if self._saldo >= valor:
                # tiro o valor do saldo escondido
                self._saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                # se não tiver saldo, erro pra avisar
                raise ValueError("Saldo insuficiente para realizar o saque.")
        else:
            # se tentar sacar negativo ou zero
            print("Valor de saque deve ser positivo.")

    # Função simples só pra mostrar o saldo atual
    def consultar_saldo(self):
        # uso o saldo formatado bonito
        print(f"Saldo atual: {self.saldo}")

    # Isso roda quando faço print(conta)
    def __str__(self):
        # monto uma frase legal com nome e saldo
        return f"Conta de {self.titular} - Saldo: {self.saldo}"

    # Isso é mais pro debug (quando printo no console ou em lista)
    def __repr__(self):
        # mostro como criar a conta de novo
        return f"ContaBancaria(titular={self.titular!r}, saldo={self._saldo})"

    # Isso deixa eu somar duas contas: conta1 + conta2
    def __add__(self, outra_conta):
        # verifico se a outra coisa é mesmo uma conta bancária
        if not isinstance(outra_conta, ContaBancaria):
            # se não for, devolvo isso pro Python lidar
            return NotImplemented
        # somo os saldos reais (números normais, sem R$)
        return self._saldo + outra_conta._saldo


# Aqui começa a parte de testes (só roda se eu executar esse arquivo)
if __name__ == "__main__":
    # crio duas contas pra testar tudo
    conta1 = ContaBancaria("Pedro", 300)   # começa com 300
    conta2 = ContaBancaria("Ana", 450)     # começa com 450

    # mostro a conta1 pra ver se o print ficou bonito
    print(conta1)
    
    # mostro só o saldo formatado
    print(conta1.saldo)
    
    # testo a soma das duas contas
    print(f'Soma dos saldos: R$ {conta1 + conta2:.2f}')
    
    # tento colocar saldo negativo pra ver o erro aparecer
    try:
        conta1.saldo = -100
    except ValueError as e:
        # mostro o erro que veio
        print(e)
    
    # deposito 200 na conta1
    conta1.depositar(200)
    
    # mostro o saldo novo (tem que ser 500)
    print(conta1.saldo)