from POO.meu_projeto.models.cliente import Cliente

class Funcionario(Cliente):
    def __init__(self, nome: str, sexo: str, cpf: str, telefone: str, email: str, matricula: str, funcao: str, salario: float):
        super().__init__(nome, sexo, cpf, telefone, email)
        self.matricula = matricula
        self.funcao = funcao
        self.salario = salario

