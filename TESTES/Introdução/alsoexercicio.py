sexo = input('Informe Seu Sexo (M/F): ')
H = float(input('informe Sua Altura: '))

pesoideal = 0.0

if (sexo.upper() == 'M'):
        pesoideal = (72.7*H)-58
elif(sexo.upper() == 'F'):
        pesoideal = (62.1*H)-44.7
else:
    print('Sexo Invalido.')
    
print('seu peso ideal é',sexo.upper())
print('seu peso ideal é',round(pesoideal, 2))