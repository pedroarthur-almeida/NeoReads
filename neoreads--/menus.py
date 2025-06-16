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
            print('\nOpção inválida. Tente novamente.')
            Sistema.aguardar_volta()
            continue

def menu_logado(usuario,cadastro):
    while True:
        Sistema.limpar_tela()
        print('\n-- Menu Logado --')
        print('\n📚 1. Ver perfil de leitor')
        print('🔄 2. Atualizar dados')
        print('💡 3. Buscar bibliotecas proximas')
        print('📖 4. Estimativas de leitura')
        print('❗ 5. Deletar conta')
        print('🚪 6. Sair')
        
        opcao = input('\nDigite sua opcao: ')

        if opcao == '1':
            usuario.ver_perfil()

        elif opcao == '2':
            cadastro.atualizar_dados()

        elif opcao == '3':
            pass

        elif opcao == '4':
            pass

        elif opcao == '5':
            deletado = cadastro.deletar_usuario()
            if deletado:
                print('Saindo...')
                Sistema.aguardar_volta()
                break 

        elif opcao == '6':
            saindo = input('Deseja mesmo sair? (s/n)')
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