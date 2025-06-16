import time
from config import generos_disponiveis, estados_brasileiros
from system import Sistema

class Cadastro:
    def __init__(self):
        self.usuarios = {}

    def cadastrar(self):
        while True:
            Sistema.limpar_tela()
            print('CADASTRO => Siga as instrucoes para um cadastro bem sucedido.')
            print('\n-- DADOS PESSOAIS --')
            nome = input('Digite seu nome: ')
            if self.validar_nome(nome):
                break
            else:
                continue

        while True:        
            email = input('Digite o seu email: ').lower().strip()
            if self.validar_email(email):
                break
            else:
                continue

        while True:        
            senha = input('Digite sua senha: ')
            if self.validar_senha(senha):
                print('Validando...')
                time.sleep(2)
                break
            else:
                continue

        while True:
            print('\n')
            print('-- INFORMACOES ADICIONAIS --')
            idade = int(input('Digite sua idade: '))
            if self.validar_idade(idade):
                break
            else:
                continue

        while True:
            estado = input('Digite seu estado, ex-(PE,RS,RJ): ').upper().strip()
            cidade = input('Digite sua cidade: ')
            if self.validar_estadocidade(estado,cidade):
                print('Validando...')
                time.sleep(2)
                break
            else:
                continue

        while True:
            print('\n')
            print('-- HABITOS DE LEITURA --')
            livrosdigitaislidos = input('Quantos livros digitais voce leu no ultimo ano? ')
            if livrosdigitaislidos.isdigit():
                livrosdigitaislidos = int(livrosdigitaislidos)
                if self.validar_livrosdigitaislidos(livrosdigitaislidos):
                    break
                else:
                    continue
            else:
                print('Digite somente numeros, por favor.')
                continue

        while True:
            livrosfisicoslidos = input('Quantos livros fisicos voce leu no ultimo ano? ')
            if livrosfisicoslidos.isdigit():
                livrosfisicoslidos = int(livrosfisicoslidos)
                if self.validar_livrosfisicoslidos(livrosfisicoslidos):
                    break
                else:
                    continue
            else:
                print('Digite somente numeros, por favor.')

        while True:
            preferencia = input('Qual sua preferencia de leitura? (f para livro fisico e d para livro digital)').strip().lower()
            if self.validar_preferenciadeleitura(preferencia):
                break
            else:
                continue

        while True:
            horasestudos = input('Quantas horas por semana voce dedica a leitura de livros para os seus estudos? ')
            if horasestudos.isdigit():
                horasestudos = int(horasestudos)
                if self.validar_horaslidasestudos(horasestudos):
                    break
                else:
                    continue
            else:
                print('Digite somente numeros, por favor.')
                continue

        while True:
            horasentretenimento = input('Quantas horas por semana voce dedica para a leitura de livros somente para o seu entretenimento? ')
            if horasentretenimento.isdigit():
                horasentretenimento = int(horasentretenimento)
                if self.validar_horaslidasentretenimento(horasentretenimento):
                    print('validando...')
                    time.sleep(2)
                    break
                else:
                    continue
            else:
                print('Digite somente numeros, por favor.')
                continue

        while True:
            Sistema.limpar_tela()
            print('\nAgora, preciso que escolha um genero como o seu favorito.')
            print('-- GÊNEROS DISPONÍVEIS --\n')
            for genero in generos_disponiveis:
                print(f'-> {genero.title()}')

            genero_favorito = input('\nDigite seu gênero favorito de leitura (como está acima): ').strip().lower()

            if genero_favorito in generos_disponiveis:
                break
            else:
                print('Digite um gênero válido conforme a lista acima.')

        novo_usuario = Usuario(email=email, senha=senha, nome=nome, idade=idade, cidade=cidade, estado=estado, livrosdigitais_lidos=livrosdigitaislidos, livrosfisicos_lidos=livrosfisicoslidos, preferencia_de_leitura= preferencia, horaslidas_estudo=horasestudos,horaslidas_entretenimento=horasentretenimento, genero = genero_favorito)
        self.usuarios[email] = novo_usuario
        print('\nUsuário cadastrado com sucesso!')
        Sistema.aguardar_volta()

    def validar_nome(self, nome):
        if len(nome) <= 2:
            print('Nome muito curto.')
            Sistema.aguardar_volta()
            return False
        else:
            return True

    def validar_email(self, email):
        if email in self.usuarios:
            print('Esse email ja foi cadastrado.')
            Sistema.aguardar_volta()
            return False
        elif '@' not in email or '.com' not in email:
            print('Digite um email valido. O email precisa ter ".com" e "@".')
            Sistema.aguardar_volta()
            return False
        dominios_validos = ['gmail.com', 'outlook.com', 'hotmail.com', 'yahoo.com', 'icloud.com']
        if not any(email.endswith(dominio) for dominio in dominios_validos):
            print('Dominio invalido! Use: Gmail, Outlook, Hotmail, Yahoo ou iCloud.')
            Sistema.aguardar_volta()
            return False
        else:
            return True
        
    def validar_senha(self, senha):
        if len(senha) < 6:
            print('Sua senha precisa ter, no minimo, 6 caracteres.')
            Sistema.aguardar_volta()
            return False
        else:
            return True
    
    def validar_idade(self, idade):
        if idade <= 0 or idade > 110:
            print('Idade invalida.')
            Sistema.aguardar_volta()
            return False
        else:
            return True

    def validar_estadocidade(self, estado, cidade):
        if estado not in estados_brasileiros:
            print('Digite um estado valido.')
            Sistema.aguardar_volta()
            return False
        if not cidade.replace(' ', '').isalpha() or len(cidade) == 0:
            print('Digite uma cidade valida.')
            Sistema.aguardar_volta()
            return False
        else:
            return True

    def validar_livrosdigitaislidos(self, livrosdigitaislidos):
        if int(livrosdigitaislidos) < 0:
            print('Numero invalido de livros.')
            Sistema.aguardar_volta()
            return False
        else:
            return True

    def validar_livrosfisicoslidos(self, livrosfisicoslidos):
        if int(livrosfisicoslidos) < 0:
            print('Numero invalido de livros.')
            Sistema.aguardar_volta()
            return False
        else:
            return True
    
    def validar_preferenciadeleitura(self, preferencia):
        preferencias = ['f', 'd']
        if not preferencia in preferencias:
            print('Digite uma preferencia valida. (livro digital ou livro fisico)')
            Sistema.aguardar_volta()
            return False
        else:
            return True

    def validar_horaslidasestudos(self, horasestudos):
        if horasestudos < 0:
            print('Digite horas validas.')
            Sistema.aguardar_volta()
            return False
        else:
            return True

    def validar_horaslidasentretenimento(self, horasentretenimento):
        if horasentretenimento < 0:
            print('Digite horas validas.')
            Sistema.aguardar_volta()
            return False
        else:
            return True
        
    def login(self):
        from menus import menu_logado
        Sistema.limpar_tela()
        print('Login -> Siga as instrucoes para um login bem sucedido.')
        email = input('\nDigite seu email: ').lower().strip()
        senha = input('Digite sua senha: ')
        
        usuario = self.usuarios.get(email)
        if usuario and usuario.senha == senha:
            Sistema.limpar_tela()
            print(f'Login realizado com sucesso! Bem-vindo(a), {usuario.nome}.')
            Sistema.mostrar_estatistica_leitura(usuario)
            menu_logado(usuario, self)
            return usuario
        else:
            print('Email ou senha incorretos.')
            Sistema.aguardar_volta()
            return None
        
    def deletar_usuario(self):
        while True:
            Sistema.limpar_tela()
            print('Como medida de seguranca, para prosseguir, e necessario que voce faca login novamente.\n')
            email = input('Digite seu email: ')
            senha = input('Digite sua senha: ')

            usuario = self.usuarios.get(email)
            if usuario and usuario.senha == senha:
                confirmacao = input('\nTem certeza que deseja deletar sua conta? (s/n)').strip().lower()
                if confirmacao == 's':
                    del self.usuarios[email]
                    print('\nConta deletada com sucesso.')
                    return True
                elif confirmacao == 'n':
                    print('\nOperacao cancelada.')
                    Sistema.aguardar_volta()
                    return False
                else:
                    print('Preciso que digite (s) ou (n).')
                    Sistema.aguardar_volta()
                    continue
            else:
                print('Usuario ou senha incorretos.')
                Sistema.aguardar_volta()
                continue

    def atualizar_dados(self):
        while True:
            Sistema.limpar_tela()
            print('Atualização de Dados -> Faça login para continuar.\n')
            email = input('Digite seu email: ').lower().strip()
            senha = input('Digite sua senha: ')
            
            usuario = self.usuarios.get(email)
            if usuario and usuario.senha == senha:
                while True:
                    Sistema.limpar_tela()
                    print('O que você deseja atualizar?\n')
                    print('1. Nome')
                    print('2. Senha')
                    print('3. Idade')
                    print('4. Cidade')
                    print('5. Estado')
                    print('6. Preferência de leitura')
                    print('7. Gênero favorito')
                    print('8. Voltar')

                    opcao = input('\nEscolha uma opção: ')

                    if opcao == '1':
                        novo_nome = input('Digite o novo nome: ')
                        if self.validar_nome(novo_nome):
                            usuario.nome = novo_nome
                            print('Nome atualizado com sucesso!')
                            Sistema.aguardar_volta()
                        else:
                            print('Digite um nome valido.')
                            Sistema.aguardar_volta()
                            continue

                    elif opcao == '2':
                        nova_senha = input('Digite a nova senha: ')
                        if self.validar_senha(nova_senha):
                            usuario.senha = nova_senha
                            print('Senha atualizada com sucesso!')
                            Sistema.aguardar_volta()
                        else:
                            print('Digite uma senha valida.')
                            Sistema.aguardar_volta()
                            continue

                    elif opcao == '3':
                        nova_idade = int(input('Digite a nova idade: '))
                        if self.validar_idade(nova_idade):
                            usuario.idade = nova_idade
                            print('Idade atualizada com sucesso!')
                            Sistema.aguardar_volta()
                        else:
                            print('Digite uma idade valida.')
                            Sistema.aguardar_volta()
                            continue

                    elif opcao == '4':
                        nova_cidade = input('Digite a nova cidade: ')
                        if nova_cidade.replace(' ', '').isalpha():
                            usuario.cidade = nova_cidade
                            print('Cidade atualizada com sucesso!')
                            Sistema.aguardar_volta()
                        else:
                            print('Cidade inválida.')
                            Sistema.aguardar_volta()
                            continue

                    elif opcao == '5':
                        novo_estado = input('Digite o novo estado (ex: PE, SP): ').upper().strip()
                        if novo_estado in estados_brasileiros:
                            usuario.estado = novo_estado
                            print('Estado atualizado com sucesso!')
                            Sistema.aguardar_volta()
                        else:
                            print('Estado inválido.')
                            Sistema.aguardar_volta()
                            continue

                    elif opcao == '6':
                        nova_preferencia = input('Digite sua nova preferência (f para físico, d para digital): ').lower().strip()
                        if self.validar_preferenciadeleitura(nova_preferencia):
                            usuario.preferencia_de_leitura = nova_preferencia
                            print('Preferência atualizada com sucesso!')
                            Sistema.aguardar_volta()
                        else:
                            print('Digite uma preferencia valida. (f para fisico e d para digital)')
                            Sistema.aguardar_volta()
                            continue

                    elif opcao == '7':
                        print('\nGêneros disponíveis:')
                        for genero in generos_disponiveis:
                            print(f'-> {genero.title()}')
                        novo_genero = input('Digite seu novo gênero favorito: ').lower().strip()
                        if novo_genero in generos_disponiveis:
                            usuario.genero = novo_genero
                            print('Gênero atualizado com sucesso!')
                            Sistema.aguardar_volta()
                        else:
                            print('Gênero inválido.')
                            Sistema.aguardar_volta()
                            continue

                    elif opcao == '8':
                        print('Voltando ao menu...')
                        Sistema.aguardar_volta()
                        break
                    else:
                        print('Digite uma opção válida.')
                        Sistema.aguardar_volta()
                        continue
                break  
            
            else:
                print('Email ou senha incorretos.')
                Sistema.aguardar_volta()
                continuar = input('Deseja tentar novamente? (s/n): ').strip().lower()
                if continuar == 'n':
                    break
                elif continuar == 's':
                    continue
                else:
                    print('digite (s/n)')
  
class Usuario:
    def __init__(self, email, senha, nome, idade, cidade, estado, livrosdigitais_lidos, livrosfisicos_lidos, preferencia_de_leitura, horaslidas_estudo, horaslidas_entretenimento, genero):
        self.email = email
        self.senha = senha
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.estado = estado
        self.livrosdigitais_lidos = livrosdigitais_lidos
        self.livrosfisicos_lidos = livrosfisicos_lidos
        self.preferencia_de_leitura = preferencia_de_leitura
        self.horaslidas_estudo = horaslidas_estudo
        self.horaslidas_entretenimento = horaslidas_entretenimento
        self.genero = genero 

    def ver_perfil(self):
        Sistema.limpar_tela()
        print('--- Seu Perfil de Leitor ---\n')
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Cidade: {self.cidade} - {self.estado}')
        print(f'Livros lidos (físicos): {self.livrosfisicos_lidos}')
        print(f'Livros lidos (digitais): {self.livrosdigitais_lidos}')
        print(f'Preferência de leitura: {"Físico" if self.preferencia_de_leitura == "f" else "Digital"}')
        print(f'Gênero favorito: {self.genero.title()}')
        Sistema.aguardar_volta()
