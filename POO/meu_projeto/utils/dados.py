def impressao_dados(dado,op):
    print(f'nome: {dado.nome}')
    print(f'sexo: {dado.sexo}')
    print(f'CPF: {dado.cpf}')
    print(f'telefone: {dado.telefone}')
    print(f'email: {dado.email}')
    if op == 1:
        print(f'endereço: {dado.endereco}')
        if dado.ativo:
            print(f'ativo')
        else:
            print(f'inativo')
    elif op == 2:
        print(f'matricula: {dado.matricula}')
        print(f'Função: {dado.funcao}')
        print(f'salario: {dado.salario}')   
    else:
        print('Opção incorreta!') 