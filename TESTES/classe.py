class Aluno:

    def __init__(self,nome,matricula,notas):
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
        elif self.media < 7:
            return 'C'    
        elif self.media < 9:
            return 'B'  
        elif self.media > 9:
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


aluno1 = Aluno(nome="Douglas",matricula='20231001',notas=[8,7,9])
aluno1.media = sum(aluno1.notas) / len(aluno1.notas)
aluno1.conceito = aluno1.conceito_aluno()
aluno1.resultado = aluno1.resultado_aluno()

aluno2 = Aluno(nome="Gabriel",matricula='20231002',notas=[6.5,4,3])
aluno2.media = sum(aluno2.notas) / len(aluno2.notas)
aluno2.conceito = aluno2.conceito_aluno()
aluno2.resultado = aluno2.resultado_aluno()

impressao(aluno1)
print('')
impressao(aluno2)