import os

def exibir_nome_do_programa():
    print('𝒮𝒶𝒷ℴ𝓇 ℰ𝓍𝓅𝓇ℯ𝓈𝓈\n');

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n')

opcao_escolhida = int(input('Escolha uma opção: '))

def finalizar_app():
    os.system('cls')
    print('Finalizando o App \n')

def escolher_opcao():
    if opcao_escolhida == 1:
        print('Cadastrando restaurante...')
    elif opcao_escolhida == 2:
        print('Listando restaurante...')    
    elif opcao_escolhida == 3:
        print('Ativando restaurante...') 
    else:
        finalizar_app()       

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()


