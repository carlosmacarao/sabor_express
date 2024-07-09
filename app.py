import os

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
    print('Opção inválida!')    
    input('Digite uma tecla para voltar ao menu inicial: ')
    main()

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))

    match opcao_escolhida:
        case 1:
            print('Cadastrando restaurante...')
        case 2:
            print('Listando restaurante...')
        case 3:
            print('Ativando restaurante...')
        case 4:
            finalizar_app()
        case any:
            opcao_invalida()              
 

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()


