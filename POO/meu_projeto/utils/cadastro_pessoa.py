from models.cliente import Cliente
from models.funcionario import Funcionario

def cadastro_pessoa(op):
    nome = input("Digite O Nome: ")
    sexo = input('Digite O Sexo: ')
    cpf = input('Digite o CPF: ')
    telefone = input('Digite o seu telefone: ')
    email = input('Digite o Email: ')

    cliente = None
    if op == 1:
        endereco = input('Digite o endereço: ')
        cliente = Cliente(nome, sexo, cpf, telefone, email)
        cliente.endereco = endereco
        return cliente
    elif op == 2:
        matricula = input('digite a matricula: ')
        funcao = input('digite a função: ')
        salario = float(input('digite o salario: '))
        funcionario = Funcionario(nome, sexo, cpf, telefone, email, matricula, funcao, salario)
        return funcionario
    else: 
        return None
