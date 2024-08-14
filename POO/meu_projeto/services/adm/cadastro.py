from models.produto import Produto

def cadastro():
    codigo = input('Digite o código: ')
    nome = input('Digite o nome do produto: ')
    quant = int(input('Digite a quantidade: '))
    preco = float(input('Digite o preco: '))

    produto = Produto(codigo, nome, quant, preco)

    return produto