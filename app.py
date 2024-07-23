import os

restaurantes = [
   { 'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
   { 'nome':'Pizza Suprema', 'categoria':'Italiana', 'ativo':True},
   { 'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}
]

def exibir_nome_do_programa():
    print('𝒮𝒶𝒷ℴ𝓇 ℰ𝓍𝓅𝓇ℯ𝓈𝓈 \n')

def exibir_opcoes():
    print('1. Cadastrar restaurante ')
    print('2. Listar restaurante ')
    print('3. Alterar estado do restaurante ')
    print('4. Sair. \n')

def voltar_ao_menu_principal():
    input('\n Digite uma tecla para voltar ao menu inicial: ')
    main()


def finalizar_app():
    exibir_subtitulo('Finalizando o App!')
    #print('Finalizando o App! \n')


def opcao_invalida():
    '''Esta é a função que mostra a opção inválida'''
    
    print('\n Opção inválida!')    
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função é responsável por exibir o subtitulo em cada uma das opções selecionadas'''

    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()
    

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante'''

    exibir_subtitulo('=======Cadastro de novos restaurantes=======')   
    #print('======Cadastro de novos restaurantes====== \n')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria = input('Digite o nome da categoria do restaurante {}: '.format(nome_do_restaurante))
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print('Restaurante {} cadastrado com sucesso! \n'.format(nome_do_restaurante))
    voltar_ao_menu_principal()
    

def listar_restaurantes():
    '''Essa é a função responsável por listar os restaurantes cadastrados.'''

    exibir_subtitulo('=======Lista de Restaurantes=======')
    #print('======Lista de Restaurantes====== \n')  

    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print('. {} | {} | {}'.format(nome_restaurante.ljust(20), categoria.ljust(20), ativo))


    voltar_ao_menu_principal()

def alterar_estado_restaurante():
    '''Esta é a função responsável por mostrar o status de cada restaurante cadastrado.'''

    exibir_subtitulo('Alterando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = 'O restaurante {} foi ativado com sucesso'.format(nome_restaurante) if restaurante['ativo'] else 'O restaurante {} foi desativado com sucesso!'.format(nome_restaurante)
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')


    voltar_ao_menu_principal()
    

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alterar_estado_restaurante()
            case 4:
                finalizar_app()
            case any:
                opcao_invalida()   
    except:
        opcao_invalida()                       
 

def main():
    '''FunçÃo principal do programa'''

    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()


