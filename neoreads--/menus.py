from user_management import Cadastro
from system import Sistema

cadastro = Cadastro()
sistema = Sistema()

def menu_inicial():
     while True:
        Sistema.limpar_tela()
        print('\n-- Menu Inicial --')
        print('\n1. Cadastrar novo usuário')
        print('2. Login')
        print('3. Sair')

        opcao = input('\nEscolha uma opção: ')

        if opcao == '1':
            cadastro.cadastrar()
        elif opcao == '2':
            cadastro.login()
        elif opcao == '3':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')

def menu_logado(usuario):
    while True:
        Sistema.limpar_tela()
        print('\n-- Menu Logado --')
        print('\n📚 1. Ver perfil de leitor')
        print('🔄 2. Atualizar dados')
        print('💡 3. Buscar bibliotecas proximas')
        print('❗ 4. Deletar conta')
        print('🚪 5. Sair')
        
        opcao = input('\nDigite sua opcao: ')

        if opcao == '1':
            usuario.ver_perfil()
        elif opcao == '2':
            pass
        elif opcao == '3':
            pass
        elif opcao == '4':
            pass
        elif opcao == '5':
            saindo = ('Deseja mesmo sair? (s/n)')
            if saindo == 's':
                print('Saindo...')
                break
            elif saindo == 'n':
                pass
            else:
                print('Digite (s) ou (n).')
                pass
        else:
            print('Digite uma opcao valida.')
            Sistema.aguardar_volta()
            continue