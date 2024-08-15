
class Aluno:

    def __init__(self,nome,matricula,notas = []):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas
        self.conceito = ''
        self.media = 0
        self.resultado = ''

    def conceito_aluno(self):
        if self.media < 4:
            return 'E'
        elif self.media < 6:
            return 'D'
        elif self.media < 7.5:
            return 'C'    
        elif self.media < 9:
            return 'B'  
        else:
            return 'A'
                
    def resultado_aluno(self):
        if self.conceito == 'A' or self.conceito == 'B' or self.conceito == 'C':
            return 'APROVADO'
        else:
            return 'REPROVADO'
        
def impressao(aluno):
    print(f'Aluno: {aluno.nome}')
    print(f'Matricula: {aluno.matricula}')
    print(f'Notas: {aluno.notas}')
    print(f'Media: {round(aluno.media, 1)}')
    print(f'Conceito: {aluno.conceito}')
    print(f'Resultado: {aluno.resultado}')    
        
alunos = []
while True:
    notas = []
    nome = input('Digite o nome: ')
    matricula = input('Digite sua matricula: ')
    for i in range(3):
        nota = float(input(f'Digite a nota {i+1}: '))
        notas.append(nota)
    aluno = Aluno(nome, matricula, notas)
    aluno.media = sum(aluno.notas) / len(aluno.notas)
    aluno.conceito = aluno.conceito_aluno()
    aluno.resultado = aluno.resultado_aluno()
    alunos.append(aluno)

    sair = input('Digite S para Sair Ou enter para continuar: ')

    if sair.upper()== 'S':
        break

for aluno in alunos:
    print('')
    impressao(aluno)
    print('')

busca = input('Digite a matricula que busca: ')

for aluno in alunos:
    if busca == aluno.matricula:
        print('')
        impressao(aluno)
        print('')
        break
