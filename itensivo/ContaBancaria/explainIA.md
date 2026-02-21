# Aula: Entendendo a classe ContaBancaria do zero ao avançado

**Objetivo da aula hoje:**  
Você vai sair sabendo exatamente o que cada linha faz, por que colocamos cada coisa e como isso se conecta com Python "de verdade" (não só tutorialzinho).

## 1. O que é essa classe mesmo? (visão geral)

Essa classe é como um **molde** para criar contas de banco.  
Cada vez que você faz `ContaBancaria("Pedro", 300)`, você cria um objeto (uma conta específica).

Dentro desse objeto tem:

- Nome do dono
- Saldo (dinheiro)
- Regras: não pode ficar negativo, depósito positivo, etc.
- Jeitos especiais de usar: `print(conta)`, `conta1 + conta2`, `conta.saldo = 1000` (com proteção)

## 2. O começo: `__init__` (o "nascimento" da conta)

```python
def __init__(self, titular, saldo_inicial=500):
    self._titular = titular
    self._saldo = saldo_inicial
```

- `__init__` é chamado automaticamente quando você faz `ContaBancaria(...)`
- `self` é o próprio objeto que está nascendo (tipo "eu mesmo")
- `titular` e `saldo_inicial` são informações que você passa
- O `=500` significa "se não passar nada, começa com 500"
- Colocamos underline `_` antes do nome porque é uma convenção: "esse valor é interno, não mexa diretamente nele"
- É como colocar um aviso: "só mexa usando os botões que eu criei"

## 3. Property: fazendo atributos "bonitos" e protegidos

```python
@property
def titular(self):
    return self._titular

@property
def saldo(self):
    return f"R$ {self._saldo:.2f}"
```

- `@property` transforma um método em algo que parece atributo normal
- Antes: você teria que fazer `conta.get_saldo()` (chato)
- Depois: `conta.saldo` (parece atributo simples, mas roda código por trás)
- No saldo, nós formatamos o número pra ficar bonito (R$ 123.45)
- Importante: isso é só leitura. Não dá pra fazer `conta.saldo = 1000` ainda (por enquanto só mostra)

## 4. O setter: protegendo o saldo de verdade

```python
@saldo.setter
def saldo(self, valor):
    if valor < 0:
        raise ValueError("Não pode colocar saldo negativo!")
    self._saldo = valor
```

- `@saldo.setter` roda quando alguém tenta `conta.saldo = 1000`
- Nós checamos: se o valor for negativo → erro! (o programa para e avisa)
- Se for ok → mudamos o `_saldo` de verdade
- Por que `raise ValueError` e não só `print`?
  - Porque `print` alguém pode ignorar. `raise` força quem usa a classe a tratar o problema (`try/except`)

## 5. Métodos normais: depositar e sacar

```python
def depositar(self, valor):
    if valor > 0:
        self._saldo += valor
        print(f"Depósito de R${valor:.2f} feito!")
    else:
        print("Valor de depósito deve ser positivo.")
```

- Simples: checa se positivo → soma no saldo escondido → avisa que deu certo

```python
def sacar(self, valor):
    if valor > 0:
        if self._saldo >= valor:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")
        else:
            raise ValueError("Saldo insuficiente!")
    else:
        print("Valor de saque deve ser positivo.")
```

- Mesma lógica, mas com duas checagens: positivo + saldo suficiente
- Usamos `raise` de novo pra ser consistente: erro grave = `raise`

## 6. As mágicas do Python: `__str__`, `__repr__`, `__add__`

**`__str__`: o que aparece quando você faz `print(conta)`**

```python
def __str__(self):
    return f"Conta de {self.titular} - Saldo: {self.saldo}"
```

→ bonito para humanos

**`__repr__`: o que aparece no debug ou quando printa lista de objetos**

```python
def __repr__(self):
    return f"ContaBancaria({self.titular!r}, {self._saldo})"
```

→ útil pra programador ver como recriar o objeto

**`__add__`: permite o operador `+`**

```python
def __add__(self, outra):
    if not isinstance(outra, ContaBancaria):
        return NotImplemented
    return self._saldo + outra._saldo
```

→ `conta1 + conta2` vira soma dos saldos (retorna número, não nova conta)

## 7. O bloco de teste (`if __name__ == "__main__"`)

```python
if __name__ == "__main__":
    # testes aqui
```

- Isso roda só se você executar o arquivo direto (`python main.py`)
- Se alguém importar sua classe em outro arquivo, os testes não rodam (boa prática)