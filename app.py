import os

restaurantes = [
    'Pizza',
    'Hamburguer',
    'Sushi'
]

def exibir_nome_do_programa():
    print('𝒮𝒶𝒷ℴ𝓇 ℰ𝓍𝓅𝓇ℯ𝓈𝓈\n');

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n')


def finalizar_app():
    os.system('cls')
    print('Finalizando o App! \n')

def opcao_invalida():
    print('\nOpção inválida!')    
    input('Digite uma tecla para voltar ao menu inicial: ')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')   
    print('======Cadastro de novos restaurantes====== \n')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print('Restaurante {} cadastrado com sucesso! \n'.format(nome_do_restaurante))
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def listar_restaurantes():
    os.system('cls')
    print('======Lista de Restaurantes====== \n')  

    for restaurante in restaurantes:
        print('.Restaurante {}'.format(restaurante))

    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativando restaurante...')
            case 4:
                finalizar_app()
            case any:
                opcao_invalida()   
    except:
        opcao_invalida()                       
 

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()


