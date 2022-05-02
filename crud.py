from dao import Banco
import msvcrt as m
from datetime import date

def wait():
    m.getch()

class Acesso:
    def cadastrarUsuario():
        print('Vamos cadastrar um novo usuário!\n')
        print('Para retornar ao menu a qualquer momento, digite "MENU".')
        print('> APERTE QUALQUER TECLA PARA CONTINUAR')
        wait()
        
        evasao = ['exit', 'menu']
        users = Banco.Usuario()
        users = users.buscarUsuarios()

        while True:
            print('Qual é o seu username?')
            resposta = input().lower()
            resposta = resposta.replace(' ', '')
            print()

            if resposta not in evasao:
                if len(resposta) <= 20 and resposta not in users:
                    username = resposta
                    break
                else:
                    print(f"Erro: Username '{resposta}' inválido.\n")
            else:
                if evasao[0] == resposta:
                    quit()
                elif evasao[1] == resposta:
                    return
        
        while True:
            print('Qual é o seu nome?')
            resposta = input()
            print()

            if resposta not in evasao:
                if len(resposta) <= 45 and len(resposta) > 2:
                    nome = resposta
                    break
                else:
                    print(f"Erro: Nome '{resposta}' inválido.\n")
            else:
                if evasao[0] == resposta:
                    quit()
                elif evasao[1] == resposta:
                    return

        while True:
            print('Qual é a sua bio? (Opcional)')
            print('Caso não queira adicionar uma bio, aperte ENTER.')
            resposta = input()
            print()

            if resposta not in evasao:
                if resposta == '':
                    bio = None
                    break
                elif len(resposta) <= 300:
                    bio = resposta
                    break
                else:
                    print(f"Erro: Nome '{resposta}' inválido.\n")
            else:
                if evasao[0] == resposta:
                    quit()
                elif evasao[1] == resposta:
                    return

        while True:
            print('Qual é a sua cidade? (Opcional)')
            print('Caso não queira adicionar uma cidade, aperte ENTER.')
            resposta = input()
            print()

            if resposta not in evasao:
                if resposta == '':
                    cidade = None
                    break
                elif len(resposta) <= 45:
                    cidade = resposta
                    break
                else:
                    print(f"Erro: Nome '{resposta}' inválido.\n")
            else:
                if evasao[0] == resposta:
                    quit()
                elif evasao[1] == resposta:
                    return

        while True:
            print('Qual é o seu país? (Opcional)')
            print('Caso não queira adicionar um país, aperte ENTER.')
            resposta = input()
            print()

            if resposta not in evasao:
                if resposta == '':
                    pais = None
                    break
                elif len(resposta) <= 45:
                    pais = resposta
                    break
                else:
                    print(f"Erro: Nome '{resposta}' inválido.\n")
            else:
                if evasao[0] == resposta:
                    quit()
                elif evasao[1] == resposta:
                    return
        
        usuario = Banco.Usuario(username=username, nome=nome,
                                bio=bio, cidade=cidade, pais=pais)
        try:
            usuario.inserirObjeto()
        except:
            print('Ocorreu um erro ao cadastrar o usuario...\n')
        else:
            print('O usuario foi cadastrado com sucesso!\n')
            return

    def atualizarPerfil():
        print('Vamos atualizar o seu perfil!\n')
        print('Para retornar ao menu a qualquer momento, digite "MENU".')
        print('> APERTE QUALQUER TECLA PARA CONTINUAR')
        wait()
        
        evasao = ['exit', 'menu']
        users = Banco.Usuario()
        users = users.buscarUsuarios()

        while True:
            print('Qual é o seu username?')
            resposta = input()

            if resposta in users:
                username = resposta
                break
        
        usuario = Banco.Usuario(username=username)
        l = usuario.buscarPorUsername()
        usuario = Banco.Usuario(*l[1:])
        usuario.setIdUsuario(l[0])

        opcoes = [
            '   1. Username',
            '   2. Nome',
            '   3. Bio',
            '   4. Cidade',
            '   5. Pais'
        ]
        print("Seu perfil está assim:\n")
        usuario.printPerfil()
        print()
        print('> APERTE QUALQUER TECLA PARA CONTINUAR')
        wait()
        
        while True:
            print("O que você deseja alterar?")
            for i in opcoes:
                print(i)
            print('Digite o numero correspondente a ação desejada.')
            choice = input().lower()
            try:
                k = int(choice)
            except:
                if 'exit' == choice:
                    quit()
                elif 'menu' == choice:
                    return
                else:
                    print(f"Erro: Comando '{choice}' inválido.\n")
            else:
                if k in range(1,6):
                    break

        if k == 1:
            while True:
                print('Qual é o seu novo username?')
                resposta = input()
                if resposta.lower() not in evasao:
                    if len(resposta) in range(1, 21) and resposta not in users:
                        usuario.setUsername(resposta)
                        break
                else:
                    if evasao[0] == choice:
                        quit()
                    elif evasao[1] == choice:
                        return

        elif k == 2:
            while True:
                print('Qual é o seu novo nome?')
                resposta = input()
                if resposta.lower() not in evasao:
                    if len(resposta) in range(1, 46):
                        usuario.setNome(resposta)
                        break
                else:
                    if evasao[0] == choice:
                        quit()
                    elif evasao[1] == choice:
                        return

        elif k == 3:
            while True:
                print('Qual é a sua nova bio?')
                resposta = input()
                if resposta.lower() not in evasao:
                    if resposta == '':
                        usuario.setBio(None)
                        break
                    elif len(resposta) in range(1, 301):
                        usuario.setBio(resposta)
                        break
                else:
                    if evasao[0] == choice:
                        quit()
                    elif evasao[1] == choice:
                        return

        elif k == 4:
            while True:
                print('Qual é a nova cidade?')
                resposta = input()
                if resposta.lower() not in evasao:
                    if resposta == '':
                        usuario.setCidade(None)
                        break
                    if len(resposta) in range(1, 46):
                        usuario.setCidade(resposta)
                        break
                else:
                    if evasao[0] == choice:
                        quit()
                    elif evasao[1] == choice:
                        return

        elif k == 5:
            while True:
                print('Qual é o novo país?')
                resposta = input()
                if resposta.lower() not in evasao:
                    if resposta == '':
                        usuario.setPais(None)
                        break
                    if len(resposta) in range(1, 46):
                        usuario.setPais(resposta)
                        break
                else:
                    if evasao[0] == choice:
                        quit()
                    elif evasao[1] == choice:
                        return

        try:
            usuario.atualizarObjeto()
        except:
            print('Ocorreu um erro ao cadastrar o usuario...\n')
        else:
            print('O perfil foi atualizado com sucesso!\n')
            return

    def visualizarPerfil():
        print('Vamos visualizar o seu perfil!\n')
        print('Para retornar ao menu a qualquer momento, digite "MENU".')
        print('> APERTE QUALQUER TECLA PARA CONTINUAR')
        wait()
        
        evasao = ['exit', 'menu']
        users = Banco.Usuario()
        users = users.buscarUsuarios()

        while True:
            print('Qual é o seu username?')
            resposta = input()
            print()

            if resposta.lower() not in evasao:
                if resposta in users:
                    username = resposta
                    break
                else:
                    print(f"Erro: Username '{resposta}' inválido.\n")
            else:
                if evasao[0] == resposta:
                    quit()
                elif evasao[1] == resposta:
                    return

        try:
            usuario = Banco.Usuario(username=username)
            l = usuario.buscarPorUsername()
            id = l[0]
            usuario = Banco.Usuario(*l[1:])
            usuario.setIdUsuario(id)

            print('Esse é o seu perfil:\n')
            usuario.printPerfil()
            print()

        except:
            pass
        else:
            return

    def DeletarPerfil():
        print('Vamos deletar o seu perfil :(\n')
        print('Para retornar ao menu a qualquer momento, digite "MENU".')
        print('> APERTE QUALQUER TECLA PARA CONTINUAR')
        wait()
        
        evasao = ['exit', 'menu']
        users = Banco.Usuario()
        users = users.buscarUsuarios()

        while True:
            print('Qual é o seu username?')
            resposta = input()
            print()

            if resposta.lower() not in evasao:
                if resposta in users:
                    username = resposta
                    break
                else:
                    print(f"Erro: Username '{resposta}' inválido.\n")
            else:
                if evasao[0] == resposta:
                    quit()
                elif evasao[1] == resposta:
                    return

        try:
            usuario = Banco.Usuario(username=username)
            l = usuario.buscarPorUsername()
            id = l[0]
            usuario.setIdUsuario(id)

            usuario.apagarObjeto()
            print('Seu usuario foi apagado :(\n')
            print()
            
        except:
            pass
        else:
            return

    def publicarReview():
        print('Vamos publicar uma review!\n')
        print('Para retornar ao menu a qualquer momento, digite "MENU".')
        print('> APERTE QUALQUER TECLA PARA CONTINUAR')
        wait()
        
        evasao = ['exit', 'menu']
        users = Banco.Usuario()
        users = users.buscarUsuarios()

        while True:
            print('Qual é o seu username?')
            resposta = input()
            print()

            if resposta.lower() not in evasao:
                if resposta in users:
                    username = resposta
                    break
                else:
                    print(f"Erro: Username '{resposta}' inválido.\n")
            else:
                if evasao[0] == resposta:
                    quit()
                elif evasao[1] == resposta:
                    return

        usuario = Banco.Usuario(username=username)
        l = usuario.buscarPorUsername()
        id = l[0]

        livro = Banco.Livro()
        livro = livro.mostrarTodosLivros()

        while True:
            print('Você deseja escrever uma review sobre qual dos livros?')
            print('Digite o numero correspondente a ação desejada.')
            resposta = input()
            print()

            if resposta.lower() not in evasao:
                try:
                    k = int(resposta)
                except:
                    pass
                else:
                    if k in range(1, len(livro)+1):
                        break
                    else:
                        print(f"Erro: Username '{resposta}' inválido.\n")
            else:
                if evasao[0] == resposta:
                    quit()
                elif evasao[1] == resposta:
                    return

        while True:
            print(f'Escreva a sua review do livro "{livro[k-1][0]}"!')
            resposta = input()
            print()

            if resposta.lower() not in evasao:
                if len(resposta) in range(1, 2000+1):
                    conteudo = resposta
                    break
            else:
                if evasao[0] == resposta:
                    quit()
                elif evasao[1] == resposta:
                    return

        while True:
            print(f'Dê uma nota de 1 a 5 para o livro "{livro[k-1][0]}"!')
            resposta = input()
            print()

            if resposta.lower() not in evasao:
                try:
                    r = int(resposta)
                except:
                    pass
                else:
                    if r in range(1, 6):
                        rating = r
                        break
            else:
                if evasao[0] == resposta:
                    quit()
                elif evasao[1] == resposta:
                    return
        
        try:
            review = Banco.Review(conteudo=conteudo, data_postagem=str(date.today()),
                                rating=rating, idLivro=k, idUsuario=id)
            review.inserirObjeto()
            print('Sucesso: sua review foi publicada!')

        except:
            pass
        else:
            return

    def visualizarReviews():
        print('Vamos visualizar as suas reviews!\n')
        print('Para retornar ao menu a qualquer momento, digite "MENU".')
        print('> APERTE QUALQUER TECLA PARA CONTINUAR')
        wait()
        
        evasao = ['exit', 'menu']
        users = Banco.Usuario()
        users = users.buscarUsuarios()

        while True:
            print('Qual é o seu username?')
            resposta = input()
            print()

            if resposta not in evasao:
                if len(resposta) <= 20 and resposta in users:
                    username = resposta
                    break
                else:
                    print(f"Erro: Nome '{resposta}' inválido.\n")
            else:
                if evasao[0] == resposta:
                    quit()
                elif evasao[1] == resposta:
                    return
            
        try:
            usuario = Banco.Usuario(username=username)
            l = usuario.buscarPorUsername()
            id = l[0]

            review = Banco.Review()
            review.setIdUsuario(id)
            l = review.buscarReviewsUsuario()
        except:
            pass
        else:
            for i in l:
                print(f"Nome: {i[0]}")
                print(f"Username: {i[1]}")
                print(f"Nome do Livro: {i[2]}")
                print(f"Data da Postagem: {i[3]}")
                print(f"Rating: {i[4]}")
                print(f"Conteúdo da Review: {i[5]}")
                print()
            
            return

    def menuPrincipal():
        opcoes = [
            '   1. Cadastrar seu Usuario',
            '   2. Atualizar seu Usuario',
            '   3. Visualizar seu Usuario',
            '   4. Deletar seu Usuario',
            '   5. Publicar uma Review',
            '   6. Visualizar minhas Reviews'
        ]

        while True:
            print("Olá! Bem vindo ao Menu!")
            print("O que você deseja fazer agora?")
            print('> APERTE QUALQUER TECLA PARA CONTINUAR')
            wait()
            for i in opcoes:
                print(i)
            print('Digite o numero correspondente a ação desejada.')
            choice = input().lower()
            try:
                k = int(choice)
            except:
                if 'exit' in choice:
                    quit()
                else:
                    print(f"Erro: Comando '{choice}' inválido.\n")
            else:
                if k == 1:
                    Acesso.cadastrarUsuario()
                elif k == 2:
                    Acesso.atualizarPerfil()
                elif k == 3:
                    Acesso.visualizarPerfil()
                elif k == 4:
                    Acesso.DeletarPerfil()
                elif k == 5:
                    Acesso.publicarReview()
                elif k == 6:
                    Acesso.visualizarReviews()
                else:
                    print(f"Erro: Comando '{choice}' inválido.\n")

Acesso.menuPrincipal()