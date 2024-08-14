from utils.impressao import impressao

def reajuste_produto(produtos):
    print('###### Reajuste de Produto ########')
    busca = input('Digite o código do produto: ')
    perc = None
    achei = None
    preco_reajustado = 0.0
    for produto in produtos:
        if busca == produto.codigo:
            achei = produto
            perc = float(input('Digite o percentual do aumento: '))
            preco_reajustado = produto.reajuste(perc)
            produto.preco = preco_reajustado
            break
    if achei is not None:
        impressao(achei)
    else:
        print('Produto não encontrado!')