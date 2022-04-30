import mysql.connector
from mysql.connector import Error

class Banco:
    def getConexao():
        db = mysql.connector.connect(user='root', password='0000',
                                            host='localhost',
                                            database='projeto_final')
        return db

    def executarQuery(db, query, parametros, table):
        cursor = db.cursor()
        cursor.execute(query, parametros)
        db.commit()

        try:
            return cursor.lastrowid
        except:
            pass

    class Usuario:
        def __init__(self, username=None,
                    nome=None, bio=None, cidade=None, pais=None):
            self.idUsuario = None
            self.username = username
            self.nome = nome
            self.bio = bio
            self.cidade = cidade
            self.pais = pais
            self.table = "Usuario"

        def setIdUsuario(self, newIdUsuario):
            self.idUsuario = newIdUsuario

        def setUsername(self, newUsername):
            self.username = newUsername

        def setNome(self, newNome):
            self.nome = newNome

        def setBio(self, newBio):
            self.bio = newBio

        def setCidade(self, newCidade):
            self.cidade = newCidade

        def setPais(self, newPais):
            self.pais = newPais

        def inserirObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""INSERT INTO {self.table} (username, nome, bio, cidade, pais)
                        VALUES (%s,%s,%s,%s,%s);"""
                parametros = (self.username, self.nome,
                                self.bio, self.cidade, self.pais)
                idInsert = Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
                return idInsert
        
        def apagarObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                DELETE FROM {self.table}
                WHERE id{self.table} = %s;
                """
                parametros = (self.idUsuario,)
                Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()

        def atualizarObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                UPDATE {self.table} 
                SET
                    username = %s,
                    nome = %s,
                    bio = %s,
                    cidade = %s,
                    pais = %s
                WHERE
                    idUsuario = %s;
                """
                parametros = (self.username, self.nome, self.bio,
                                self.cidade, self.pais, self.idUsuario)
                Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
        
        def buscarPorChavePrimariaObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT *
                FROM {self.table}
                WHERE id{self.table} = %s;
                """
                parametros = (self.idUsuario,)
                cursor = db.cursor()
                cursor.execute(query, parametros)
                registro = cursor.fetchall()
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)
        
        def buscarPorUsername(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT *
                FROM {self.table}
                WHERE username = %s;
                """
                parametros = (self.username,)
                cursor = db.cursor()
                cursor.execute(query, parametros)
                registro = cursor.fetchone()
                
                db.close()

                return registro

            except Error as e:
                print(e)

        def buscarUsuarios(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT username
                FROM {self.table}
                """
                parametros = ()
                cursor = db.cursor()
                cursor.execute(query, parametros)
                registro = cursor.fetchall()
                l = []
                for i in registro:
                    l.append(i[0])
                
                db.close()

                return l

            except Error as e:
                print(e)

        def buscarTodosObjetos(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT * FROM {self.table};
                """
                parametros = ()
                cursor = db.cursor()
                cursor.execute(query, parametros)
                registro = cursor.fetchall()
                for i in registro:
                    print(i)

                db.close()

                return list(registro)

            except Error as e:
                print(e)

        def printPerfil(self):
            print(f"Username: {self.username}")
            print(f"Nome: {self.nome}")
            print(f"Bio: {self.bio}")
            print(f"Cidade: {self.cidade}")
            print(f"Pais: {self.pais}")

    class Autor:
        def __init__(self, nomeAutor=None, biografia=None,
                    website=None, twitter=None, data_nascimento=None):
            self.idAutor = None
            self.nomeAutor = nomeAutor
            self.biografia = biografia
            self.website = website
            self.twitter = twitter
            self.data_nascimento = data_nascimento
            self.table = "Autor"

        def setIdAutor(self, newAutor):
            self.idAutor = newAutor
        
        def setNome(self, newNome):
            self.nomeAutor = newNome

        def setBiografia(self, newBiografia):
            self.biografia = newBiografia

        def setWebsite(self, newWebsite):
            self.website = newWebsite

        def setTwitter(self, newTwitter):
            self.twitter = newTwitter

        def setDataNascimento(self, newDataNascimento):
            self.data_nascimento = newDataNascimento

        def inserirObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""INSERT INTO {self.table} (nomeAutor, biografia, website, twitter, data_nascimento)
                        VALUES (%s,%s,%s,%s,%s);"""
                parametros = (self.nomeAutor, self.biografia, self.website, self.twitter, self.data_nascimento)

                idInsert = Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
                return idInsert
        
        def apagarObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                DELETE FROM {self.table}
                WHERE id{self.table} = %s;
                """
                parametros = (self.idAutor,)
                Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()

        def atualizarObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                UPDATE {self.table} 
                SET
                    nomeAutor = %s,
                    biografia = %s,
                    website = %s,
                    twitter = %s,
                    data_nascimento = %s
                WHERE
                    idAutor = %s;
                """
                parametros = (self.nomeAutor, self.biografia, self.website,
                                self.twitter, self.data_nascimento, self.idAutor)
                Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
        
        def buscarPorChavePrimariaObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT *
                FROM {self.table}
                WHERE id{self.table} = %s;
                """
                parametros = (self.idAutor,)
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)
        
        def buscarTodosObjetos(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT * FROM {self.table};
                """
                parametros = ()
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)

    class Editora:
        def __init__(self, nomeEditora=None,
                    sobre=None, ano_fundacao=None):
            self.idEditora = None
            self.nomeEditora = nomeEditora
            self.sobre = sobre
            self.ano_fundacao = ano_fundacao
            self.table = "Editora"
        
        def setIdEditora(self, newIdEditora):
            self.idEditora = newIdEditora

        def setNome(self, newNome):
            self.nomeEditora = newNome

        def setSobre(self, newSobre):
            self.sobre = newSobre

        def setAnoFundacao(self, newAnoFundacao):
            self.ano_fundacao = newAnoFundacao

        def inserirObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""INSERT INTO {self.table} (nomeEditora, sobre, ano_fundacao)
                        VALUES (%s,%s,%s);"""
                parametros = (self.nomeEditora, self.sobre, self.ano_fundacao)
                idInsert = Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
                return idInsert
        
        def apagarObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                DELETE FROM {self.table}
                WHERE id{self.table} = %s
                """
                parametros = (self.idEditora,)
                Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()

        def atualizarObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                UPDATE {self.table}
                SET
                    nomeEditora = %s,
                    sobre = %s,
                    ano_fundacao = %s
                WHERE
                    id{self.table} = %s;
                """
                parametros = (self.nomeEditora, self.sobre, self.ano_fundacao, self.idEditora)
                Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
        
        def buscarPorChavePrimariaObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT *
                FROM {self.table}
                WHERE id{self.table} = %s;
                """
                parametros = (self.idEditora,)
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)
        
        def buscarTodosObjetos(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT * FROM {self.table};
                """
                parametros = ()
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)

    class Genero:
        def __init__(self, nomeGenero=None):
            self.idGenero = None
            self.nomeGenero = nomeGenero
            self.table = "Genero"
        
        def setIdGenero(self, newIdGenero):
            self.idGenero = newIdGenero

        def setNome(self, newNome):
            self.nomeGenero = newNome

        def inserirObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""INSERT INTO {self.table} (nomeGenero)
                        VALUES (%s);"""
                parametros = (self.nomeGenero,)
                idInsert = Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
                return idInsert
        
        def apagarObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                DELETE FROM {self.table}
                WHERE id{self.table} = %s
                """
                parametros = (self.idGenero,)
                Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()

        def atualizarObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                UPDATE {self.table}
                SET
                    nomeGenero = %s
                WHERE
                    id{self.table} = %s;
                """
                parametros = (self.nomeGenero, self.idGenero)
                Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
        
        def buscarPorChavePrimariaObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT *
                FROM {self.table}
                WHERE id{self.table} = %s;
                """
                parametros = (self.idGenero,)
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)
        
        def buscarTodosObjetos(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT * FROM {self.table};
                """
                parametros = ()
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)

    class Livro:
        def __init__(self, nomeLivro=None, rating_media=None,
                    capa=None, data_publicacao=None, sinopse=None,
                    idAutor=None, idEditora=None, idGenero=None):
            self.idLivro = None
            self.nomeLivro = nomeLivro
            self.rating_media = rating_media
            self.capa = capa
            self.data_publicacao = data_publicacao
            self.sinopse = sinopse
            self.idAutor = idAutor
            self.idEditora = idEditora
            self.idGenero = idGenero
            self.table = "Livro"
        
        def setIdLivro(self, newIdLivro):
            self.idLivro = newIdLivro

        def setNome(self, newNome):
            self.nomeLivro = newNome

        def setRatingMedia(self, newRatingMedia):
            self.rating_media = newRatingMedia

        def setCapa(self, newCapa):
            self.capa = newCapa

        def setDataPublicacao(self, newDataPublicacao):
            self.data_publicacao = newDataPublicacao

        def setSinopse(self, newSinopse):
            self.sinopse = newSinopse

        def setIdAutor(self, newIdAutor):
            self.idAutor = newIdAutor

        def setIdEditora(self, newIdEditora):
            self.idEditora = newIdEditora

        def setIdGenero(self, newIdGenero):
            self.idGenero = newIdGenero

        def inserirObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""INSERT INTO {self.table} (nomeLivro, rating_media, capa, data_publicacao, sinopse, idAutor, idEditora, idGenero)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"""
                parametros = (self.nomeLivro, self.rating_media, self.capa,
                                self.data_publicacao, self.sinopse, self.idAutor,
                                self.idEditora, self.idGenero)
                
                cursor = db.cursor()
                cursor.execute(query, parametros)
                db.commit()

                idInsert = cursor.lastrowid
                    
            except Error as e:
                print(e)

            else:
                db.close()
                return idInsert
        
        def apagarObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                DELETE FROM {self.table}
                WHERE id{self.table} = %s;
                """
                parametros = (self.idLivro,)
                Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()

        def atualizarObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                UPDATE {self.table}
                SET
                    nomeLivro = %s,
                    rating_media = %s,
                    capa = %s,
                    data_publicacao = %s,
                    sinopse = %s,
                    idAutor = %s,
                    idEditora = %s,
                    idGenero = %s
                WHERE
                    id{self.table} = %s;
                """
                parametros = (self.nomeLivro, self.rating_media, self.capa, self.data_publicacao,
                                self.sinopse, self.idAutor, self.idEditora, self.idGenero,
                                self.idLivro)
                Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
        
        def buscarPorChavePrimariaObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT *
                FROM {self.table}
                WHERE id{self.table} = %s;
                """
                parametros = (self.idLivro,)
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)
        
        def buscarTodosObjetos(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT * FROM {self.table};
                """
                parametros = ()
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)

        def mostrarTodosLivros(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT
                    Livro.nomeLivro,
                    Autor.nomeAutor,
                    Genero.nomeGenero
                FROM Livro
                JOIN Autor
                    ON Livro.idAutor = Autor.idAutor
                JOIN Genero
                    ON Livro.idGenero = Genero.idGenero;
                """
                parametros = ()
                cursor = db.cursor()
                cursor.execute(query, parametros)
                registro = cursor.fetchall()
                
                print('No formato (Nome do Livro, Nome do Autor, Genero do Livro),')
                print('Os livros disponíveis são:\n')
                for i in range(len(registro)):
                    print(f"    {i+1}. {registro[i]}")

            except Error as e:
                print(e)
            else:
                return list(registro)

    class Review:
        def __init__(self, conteudo=None, data_postagem=None,
                    rating=None, idLivro=None, idUsuario=None):
            self.idReview = None
            self.conteudo = conteudo
            self.data_postagem = data_postagem
            self.rating = rating
            self.idLivro = idLivro
            self.idUsuario = idUsuario
            self.table = "Review"
        
        def setIdReview(self, newIdReview):
            self.idReview = newIdReview

        def setConteudo(self, newConteudo):
            self.conteudo = newConteudo

        def setDataPostagem(self, newDataPostagem):
            self.data_postagem = newDataPostagem

        def setRating(self, newRating):
            self.rating = newRating

        def setIdLivro(self, newIdLivro):
            self.idLivro = newIdLivro

        def setIdUsuario(self, newIdUsuario):
            self.idUsuario = newIdUsuario

        def inserirObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""INSERT INTO {self.table} (conteudo, data_postagem, rating, idLivro, idUsuario)
                        VALUES (%s,%s,%s,%s,%s);"""
                parametros = (self.conteudo, self.data_postagem, self.rating, self.idLivro, self.idUsuario)
                idInsert = Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
                return idInsert
        
        def apagarObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                DELETE FROM {self.table}
                WHERE id{self.table} = %s;
                """
                parametros = (self.idReview,)
                Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()

        def atualizarObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                UPDATE {self.table}
                SET
                    conteudo = %s,
                    data_postagem = %s,
                    rating = %s,
                    idLivro = %s,
                    idUsuario = %s
                WHERE
                    id{self.table} = %s;
                """
                parametros = (self.conteudo, self.data_postagem, self.rating,
                            self.idLivro, self.idUsuario, self.idReview)
                Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
        
        def buscarPorChavePrimariaObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT *
                FROM {self.table}
                WHERE id{self.table} = %s;
                """
                parametros = (self.idReview,)
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchone()
                
                db.close()

                return registro

            except Error as e:
                print(e)
        
        def buscarPorLivroUsuario(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT *
                FROM {self.table}
                WHERE idUsuario = %s
                AND idLivro = %s;
                """
                parametros = (self.idUsuario, self.idLivro)
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)

        def buscarReviewsUsuario(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT
                    Usuario.nome,
                    Usuario.username,
                    Livro.nomeLivro,
                    Review.data_postagem,
                    Review.rating,
                    Review.conteudo
                FROM Review
                JOIN usuario
                    ON Review.idUsuario = Usuario.idUsuario
                JOIN Livro
                    ON Review.idLivro = Livro.idLivro
                WHERE Review.idUsuario = %s;
                """
                parametros = (self.idUsuario,)
                cursor = db.cursor()
                cursor.execute(query, parametros)
                registro = cursor.fetchall()
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)

        def buscarTodosObjetos(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT * FROM {self.table};
                """
                parametros = ()
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)

    class Lista:
        def __init__(self, idUsuario=None,
                    nome=None, descricao=None):
            self.idLista = None
            self.idUsuario = idUsuario
            self.nome = nome
            self.descricao = descricao
            self.table = "Lista"

        def setIdLista(self, newIdLista):
            self.idLista = newIdLista
        
        def setIdUsuario(self, newIdUsuario):
            self.idUsuario = newIdUsuario

        def setNome(self, newNome):
            self.nome = newNome

        def setDescricao(self, newDescricao):
            self.descricao = newDescricao

        def inserirObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""INSERT INTO {self.table} (idUsuario, nome, descricao)
                        VALUES (%s,%s,%s);"""
                parametros = (self.idUsuario, self.nome, self.descricao)
                idInsert = Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
                return idInsert
        
        def apagarObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                DELETE FROM {self.table}
                WHERE id{self.table} = %s;
                """
                parametros = (self.idLista,)
                Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()

        def atualizarObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                UPDATE {self.table}
                SET
                    idUsuario = %s,
                    nome = %s,
                    descricao = %s
                WHERE
                    id{self.table} = %s;
                """
                parametros = (self.idUsuario, self.nome,
                                self.descricao, self.idLista)
                Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
        
        def buscarPorChavePrimariaObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT *
                FROM {self.table}
                WHERE id{self.table} = %s;
                """
                parametros = (self.idLista,)
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)
        
        def buscarTodosObjetos(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT * FROM {self.table};
                """
                parametros = ()
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)

    class Lista_has_Livro:
        def __init__(self, idLista=None, idLivro=None):
            self.idLista = idLista
            self.idLivro = idLivro
            self.table = "Lista_has_Livro"
        
        def setIdLista(self, newIdLista):
            self.idLista = newIdLista

        def setIdLivro(self, newIdLivro):
            self.idLivro = newIdLivro

        def inserirObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""INSERT INTO {self.table} (idLista, idLivro)
                        VALUES (%s,%s);"""
                parametros = (self.idLista, self.idLivro)
                idInsert = Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
                return idInsert
        
        def apagarObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                DELETE FROM {self.table}
                WHERE idLista = %s
                AND idLivro = %s;
                """
                parametros = (self.idLista, self.idLivro)
                Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
        
        def buscarPorChavePrimariaObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT *
                FROM {self.table}
                WHERE idLista = %s;
                """
                parametros = (self.idLista,)
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)
        
        def buscarTodosObjetos(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT * FROM {self.table};
                """
                parametros = ()
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)

    class Lido:
        def __init__(self, idUsuario=None):
            self.idUsuario = idUsuario
            self.table = "Lido"

        def setIdUsuario(self, newIdUsuario):
            self.idUsuario = newIdUsuario

        def inserirObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""INSERT INTO {self.table} (idUsuario)
                        VALUES (%s);"""
                parametros = (self.idUsuario,)
                idInsert = Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
                return idInsert
        
        def apagarObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                DELETE FROM {self.table}
                WHERE idUsuario = %s;
                """
                parametros = (self.idUsuario,)
                Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
        
        def buscarPorChavePrimariaObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT *
                FROM {self.table}
                WHERE idUsuario = %s;
                """
                parametros = (self.idUsuario,)
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)
        
        def buscarTodosObjetos(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT * FROM {self.table};
                """
                parametros = ()
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)

    class Lido_has_Livro:
        def __init__(self, idUsuario=None, idLivro=None):
            self.idUsuario = idUsuario
            self.idLivro = idLivro
            self.table = "Lido_has_Livro"

        def setidUsuario(self, newidUsuario):
            self.idUsuario = newidUsuario

        def setIdLivro(self, newIdLivro):
            self.idLivro = newIdLivro

        def inserirObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""INSERT INTO {self.table} (idUsuario, idLivro)
                        VALUES (%s,%s);"""
                parametros = (self.idUsuario, self.idLivro)
                idInsert = Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
                return idInsert
        
        def apagarObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                DELETE FROM {self.table}
                WHERE idUsuario = %s
                AND idLivro = %s;
                """
                parametros = (self.idUsuario, self.idLivro)
                Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()

        def buscarPorChavePrimariaObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT *
                FROM {self.table}
                WHERE idUsuario = %s;
                """
                parametros = (self.idUsuario,)
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)
        
        def buscarTodosObjetos(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT * FROM {self.table};
                """
                parametros = ()
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)

    class Lendo:
        def __init__(self, idUsuario=None):
            self.idUsuario = idUsuario
            self.table = "Lendo"

        def setIdUsuario(self, newIdUsuario):
            self.idUsuario = newIdUsuario

        def inserirObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""INSERT INTO {self.table} (idUsuario)
                        VALUES (%s);"""
                parametros = (self.idUsuario,)
                idInsert = Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
                return idInsert
        
        def apagarObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                DELETE FROM {self.table}
                WHERE id{self.table} = %s;
                """
                parametros = (self.idUsuario,)
                Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
        
        def buscarPorChavePrimariaObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT *
                FROM {self.table}
                WHERE idUsuario = %s;
                """
                parametros = (self.idUsuario,)
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)
        
        def buscarTodosObjetos(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT * FROM {self.table};
                """
                parametros = ()
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)

    class Lendo_has_Livro:
        def __init__(self, idUsuario=None, idLivro=None):
            self.idUsuario = idUsuario
            self.idLivro = idLivro
            self.table = "Lendo_has_Livro"

        def setIdUsuario(self, newIdUsuario):
            self.idUsuario = newIdUsuario

        def setIdLivro(self, newIdLivro):
            self.idLivro = newIdLivro
        
        def inserirObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""INSERT INTO {self.table} (idUsuario, idLivro)
                        VALUES (%s,%s);"""
                parametros = (self.idUsuario, self.idLivro)
                idInsert = Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
                return idInsert
        
        def apagarObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                DELETE FROM {self.table}
                WHERE idUsuario = %s
                AND idLivro = %s;
                """
                parametros = (self.idUsuario, self.idLivro)
                Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
        
        def buscarPorChavePrimariaObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT *
                FROM {self.table}
                WHERE idUsuario = %s;
                """
                parametros = (self.idUsuario,)
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)
        
        def buscarTodosObjetos(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT * FROM {self.table};
                """
                parametros = ()
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)

    class QueroLer:
        def __init__(self, idUsuario=None):
            self.idUsuario = idUsuario
            self.table = "QueroLer"

        def setIdUsuario(self, newIdUsuario):
            self.idUsuario = newIdUsuario

        def setIdUsuario(self, newIdUsuario):
            self.idUsuario = newIdUsuario

        def inserirObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""INSERT INTO {self.table} (idUsuario)
                        VALUES (%s);"""
                parametros = (self.idUsuario,)
                idInsert = Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
                return idInsert
        
        def apagarObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                DELETE FROM {self.table}
                WHERE idUsuario = %s;
                """
                parametros = (self.idUsuario,)
                Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
        
        def buscarPorChavePrimariaObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT *
                FROM {self.table}
                WHERE idUsuario = %s;
                """
                parametros = (self.idUsuario,)
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)
        
        def buscarTodosObjetos(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT * FROM {self.table};
                """
                parametros = ()
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)

    class QueroLer_has_Livro:
        def __init__(self, idUsuario=None, idLivro=None):
            self.idUsuario = idUsuario
            self.idLivro = idLivro
            self.table = "QueroLer_has_Livro"

        def setIdUsuario(self, newIdUsuario):
            self.idUsuario = newIdUsuario

        def setIdLivro(self, newIdLivro):
            self.idLivro = newIdLivro

        def inserirObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""INSERT INTO {self.table} (idUsuario, idLivro)
                        VALUES (%s,%s);"""
                parametros = (self.idUsuario, self.idLivro)
                idInsert = Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
                return idInsert
        
        def apagarObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                DELETE FROM {self.table}
                WHERE idUsuario = %s
                AND idLivro = %s;
                """
                parametros = (self.idUsuario, self.idLivro)
                Banco.executarQuery(db, query, parametros, self.table)

            except Error as e:
                print(e)
            else:
                db.close()
        
        def buscarPorChavePrimariaObjeto(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT *
                FROM {self.table}
                WHERE idUsuario = %s;
                """
                parametros = (self.idUsuario,)
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)
        
        def buscarTodosObjetos(self):
            try:
                db = Banco.getConexao()
                query = f"""
                SELECT * FROM {self.table};
                """
                parametros = ()
                cursor = db.cursor()
                cursor.execute(query, parametros)
                print(f"SUCESSO na query: {query % tuple(str(i) for i in parametros)}")
                registro = cursor.fetchall()
                for i in registro:
                    print(i)
                
                db.close()

                return list(registro)

            except Error as e:
                print(e)