import os
import platform
import random
import requests

class Sistema:
    @staticmethod
    def limpar_tela():
        sistema_operacional = platform.system()
        if sistema_operacional == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    @staticmethod
    def aguardar_volta():
        input('Tecle "enter" para retornar...')

    @staticmethod
    def buscar_livro(genero):
        try:
            url = f'https://www.googleapis.com/books/v1/volumes?q=subject:{genero}&maxResults=10'
            resposta = requests.get(url)

            if resposta.status_code == 200:
                livros = resposta.json().get('items', [])
                if livros:
                    livro_recomendado = random.choice(livros)
                    titulo = livro_recomendado['volumeInfo'].get('title', 'Título não encontrado')
                    autores = livro_recomendado['volumeInfo'].get('authors', ['Autor desconhecido'])
                    return f'Recomendação de leitura: "{titulo}" por {", ".join(autores)}'
                else:
                    return 'Não encontramos livros para esse gênero no momento.'
            else:
                return 'Erro ao buscar livros. Tente novamente mais tarde.'
        except Exception as e:
            return f'Ocorreu um erro: {e}'
    
    @staticmethod
    def mostrar_estatistica_leitura(usuario):
        media_livros_ano = 4.96
        preferencia_fisico_percent = 44
        preferencia_digital_percent = 12

        print("\n-- Estatísticas de Leitura --\n")
        if usuario.livrosdigitais_lidos + usuario.livrosfisicos_lidos > media_livros_ano:
            print(f"Parabéns! Você leu {(usuario.livrosdigitais_lidos + usuario.livrosfisicos_lidos)} livros no último ano, acima da média nacional de {media_livros_ano:.2f} livros.")
        elif usuario.livrosdigitais_lidos + usuario.livrosfisicos_lidos == media_livros_ano:
            print(f"Você está na média nacional, lendo {media_livros_ano:.2f} livros por ano.")
        else:
            print(f"Você leu {(usuario.livrosdigitais_lidos + usuario.livrosfisicos_lidos)} livros no último ano, abaixo da média nacional ({media_livros_ano:.2f}). Que tal aumentar a leitura?")

        if usuario.preferencia_de_leitura == 'f':
            print(f"Você prefere livros físicos. A preferência nacional é de {preferencia_fisico_percent}%.")
        elif usuario.preferencia_de_leitura == 'd':
            print(f"Você prefere livros digitais. A preferência nacional é de {preferencia_digital_percent}%, mas o digital cresce cada vez mais!")
        else:
            print("Preferência de leitura não reconhecida.")

        print("Fonte: Pesquisa Retratos da Leitura no Brasil (2020) - Instituto Pró-Livro\n")
        print(f'Que legal! voce gosta do genero "{usuario.genero}".')
        recomendacao = Sistema.buscar_livro(usuario.genero)
        print(recomendacao)
        Sistema.aguardar_volta()
