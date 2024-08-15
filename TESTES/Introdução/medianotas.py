while True:

    nome = input('Escreva o Seu Nome: ')

    nota1 = int(input("Escreva a Quanto Você Tirou: "))

    nota2 = int(input("Escreva a Segunda Nota: "))

    Resultado = (nota1 + nota2) /2

    if Resultado >=60:
        print (nome,("FOI APROVADO."))
        print ('SUA MEDIA FOI ',(Resultado))
    elif Resultado >=50:
        print (nome,("FICOU DE RECUPERAÇÃO."))
        print ('SUA MEDIA FOI ',(Resultado))
    else:
        print (nome,("FOI REPROVADO."))
        print ('SUA MEDIA FOI ',(Resultado))

        input('Deseja Continuar (S/N): ')
        
    