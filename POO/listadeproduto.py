class Produto:

    def __init__(self,nome,codigo,preço,quantidade):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade
        self.codigo = codigo

def impressao(produto):
    print(f'Nome: {produto.nome}')
    print(f'Codigo: {produto.codigo}')
    print(f'Preço: {produto.preço}')
    print(f'Quantidade: {produto.quantidade}')
    
produtos = []
while True:
    nome = input('Escreva o Nome do Produto: ')
    codigo = input('Escreva o Codigo: ')
    preço = input('Defina um preço: ')
    quantidade = int(input('Defina uma quantidade: '))
    produto = Produto(nome,codigo,preço,quantidade)
    produtos.append(produto)

    sair = input('Digite S para Sair Ou enter para continuar: ')

    if sair.upper()== 'S':
        break

for produto in produtos:
    print('')
    impressao(produto)
    print('')

busca = input('Digite o codigo do produto: ')

achei = ''
for produto in produtos:
    if busca == produto.codigo:
        achei = produto
        break

if achei != '':
    impressao(achei)
else:
    print('Produto desconhecido.')
    print('')
