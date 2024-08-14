def impressao(produto):
    print(f'Código: {produto.codigo}')
    print(f'Produto: {produto.nome}')
    print(f'Quantidade em estoque: {produto.quantidade}')
    print(f'Preço: {round(produto.preco, 2)}')