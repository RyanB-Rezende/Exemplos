class Produto:
    def __init__(self, codigo: str, nome: str, quantidade: int, preco: float):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def desconto(self, percentual: float):
        return self.preco - self.preco * percentual / 100
    
    def reajuste(self, percentual: float):
        return self.preco + self.preco * percentual / 100