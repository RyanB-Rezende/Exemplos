from utils.impressao import impressao

def pesquisa(produtos):
    print('####### Pesquisa de Produto ########')
    busca = input('Digite o código do produto que deseja buscar: ')
    achei = None
    for produto in produtos:
        if busca == produto.codigo:
            achei = produto
            break
        
    if achei is not None:
        impressao(achei)
    else:
        print('Produto não encontrado!')