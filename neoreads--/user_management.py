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
        print('Usuário cadastrado com sucesso!')
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
        if idade < 0 or idade > 110:
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
        email = input('Digite seu email: ').lower().strip()
        senha = input('Digite sua senha: ')
        
        usuario = self.usuarios.get(email)
        if usuario and usuario.senha == senha:
            Sistema.limpar_tela()
            print(f'Login realizado com sucesso! Bem-vindo(a), {usuario.nome}.')
            Sistema.mostrar_estatistica_leitura(usuario)
            menu_logado(usuario)
            return usuario
        else:
            print('Email ou senha incorretos.')
            Sistema.aguardar_volta()
            return None
        
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
