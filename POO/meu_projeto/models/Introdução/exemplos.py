def mensagem(a):
    print(f'SEJAM BEM VINDO(A) {a}!!!')

def dobro(x):
    return 2*x

nome = input('Qual o seu nome?: '.upper)  
mensagem(nome)  

numero = int(input('Digite um Numero: '))
print(f'o dobro de {numero} é {dobro(numero)}') 