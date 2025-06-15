from user_management import Cadastro, Sistema

cadastro = Cadastro()
sistema = Sistema()

def menu_inicial():
     while True:
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

def menu_logado():
    while True:
        print('\n-- Menu Logado --')
        print('📚 Ver perfil de leitor')
        print('🔄 Atualizar dados')
        print('💡 Buscar bibliotecas proximas')
        print('❗ Deletar conta')
        
        pass

if __name__ == '__main__':
    menu_inicial()