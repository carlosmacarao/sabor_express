idade = int(input('Qual é a sua idade? '))

if 0 <= idade <= 12:
    print('Criança!')
elif idade >= 13 and idade <= 18:
    print('Adolescente!')
else:
    print('Adulto!')        