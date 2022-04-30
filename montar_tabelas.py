from dao import Banco

def imagemParaBinario(filename):
    with open(filename, 'rb') as file:
        b = file.read()
    return b

# class Usuario:
#     def __init__(self, idUsuario=None, username=None,
#                 nome=None, bio=None, cidade=None, pais=None)

usuarios = [
    ('lariskinha', 'Larissa Rocha', 'adoro ler livros!', 'Brasilia', 'Brasil'),
    ('nowaitykatie', 'Katie Ross', 'Sempre em busca de um livro!', 'Melbourne',
    'Australia'),
    ('readwithcindy', 'Cindy', 'Leio, logo existo.', 'Sao Francisco', 'Estados Unidos'),
    ('jeonjeno', 'Lee Jeno', None, 'Busan', 'Coreia do Sul'),
    ('sabspx', 'Sabrina Peres', 'the risk i took was calculated, but man, am i bad at math',
    'Rio de Janeiro', 'Brasil')
]

for i in usuarios:
    u = Banco.Usuario(*i)
    u.inserirObjeto()

print("Usuarios:")
exibir = Banco.Usuario()
exibir.buscarTodosObjetos()
print()

# class Autor:
#     def __init__(self, idAutor=None, nome=None, biografia=None,
#                 website=None, twitter=None, data_nascimento=None)

autores = [
    ('Machado de Assis',
"""
Joaquim Maria Machado de Assis (Rio de Janeiro, 21 de junho
de 1839 – Rio de Janeiro, 29 de setembro de 1908) foi um
escritor brasileiro, considerado por muitos críticos, estudiosos,
escritores e leitores o maior nome da literatura brasileira.
Escreveu em praticamente todos os gêneros literários, sendo
poeta, romancista, cronista, dramaturgo, contista, folhetinista,
jornalista e crítico literário.
""".replace('\n', ' ')[1:-1], None, None, '1839-07-21'),
    ('Sally Rooney',
"""
Sally Rooney é uma escritora e roteirista irlandesa. Rooney
publicou três romances: "Conversas entre amigos", "Pessoas Normais";
adaptado, em 2020, para um seriado televisivo, pela Hulu e BBC,
e Belo mundo, onde você está.
""".replace('\n', ' ')[1:-1], 'https://www.faber.co.uk/author/sally-rooney/',
    'sallyrooney', '1991-02-20'),
    ('JK Rowling',
"""
Joanne "Jo" Rowling, mais conhecida como J. K. Rowling,
é uma escritora, roteirista e produtora cinematográfica britânica,
notória por escrever a série de livros Harry Potter. Os livros ganharam
uma popularidade mundial, recebendo múltiplos prêmios e vendendo
mais de 500 milhões de cópias.
""".replace('\n', ' ')[1:-1], 'https://www.jkrowling.com/', 'jk_rowling',
    '1965-07-31'),
    ('John Green',
"""
John Michael Green (Indianápolis, Indiana, 24 de agosto de 1977) é um
vlogger, empresário, produtor e autor norte-americano de livros para
jovens. Ele escreveu vários livros premiados como Looking for Alaska,
Paper Towns e The Fault in Our Stars, que foram sucesso de público e
crítica, sendo que estes dois últimos foram transformados em filmes, que
foram muito bem na bilheteria. Em 2014, Green foi listado na revista Time
como uma das "100 Pessoas mais Influentes do Mundo".
""".replace('\n', ' ')[1:-1], 'https://www.johngreenbooks.com/', 'realjohngreen',
    '1977-08-24'),
    ('Jane Austen',
"""
Jane Austen foi uma escritora inglesa. A ironia que utilizou para descrever
as personagens dos seus romances coloca-a entre os clássicos, haja vista,
a sua aceitação, inclusive na atualidade, sendo constantemente objeto de
estudo acadêmico, alcançando um público bastante amplo.
""".replace('\n', ' ')[1:-1], 'https://www.janeausten.org/', None, '1775-12-16'),
    ('Paulo Coelho',
"""
Paulo Coelho de Souza é um escritor, letrista e jornalista brasileiro. Ocupa
a cadeira 21 da Academia Brasileira de Letras. O livro O Alquimista é
considerado como um importante fenômeno literário do século XX, e já vendeu
mais de 150 milhões de cópias, superando livros como O Senhor dos Anéis e
O Pequeno Príncipe.
""".replace('\n', ' ')[1:-1], 'http://www.paulocoelhoblog.com', 'paulocoelho',
    '1947-08-24')
]

for i in autores:
    u = Banco.Autor(*i)
    u.inserirObjeto()

print("Autores:")
exibir = Banco.Autor()
exibir.buscarTodosObjetos()
print()

# class Editora:
#     def __init__(self, idEditora=None, nome=None,
#                 sobre=None, ano_fundacao=None)

editoras = [
    ('Moderna',
"""
A Editora Moderna está no mercado editorial brasileiro
desde 1968 e se orgulha de ser cada vez mais moderna.
Moderna na metodologia de ensino aplicada a todos os
livros que editamos, na tecnologia por trás das nossas obras,
no compromisso com uma educação mais dinâmica e participativa,
na motivação dos nossos colaboradores e na amplitude dos
nossos públicos atendidos.
""".replace('\n', ' ')[1:-1],
    '1968'),
    ('Rocco',
"""
A Editora Rocco é uma editora brasileira sediada na cidade
do Rio de Janeiro, fundada em 1975 por Paulo Roberto Rocco.
É mais conhecida por publicar os livros da série de Harry
Potter, Jogos Vorazes, Divergente e Eragon.
""".replace('\n', ' ')[1:-1],
    '1975'),
    ('Saraiva',
"""
Fundada em 1917 e reconhecida pelo seu pioneirismo no mercado
brasileiro, a história da Editora Saraiva iniciou-se com a
publicação de livros jurídicos, até passar a editar títulos
de outras áreas do conhecimento e obras literárias na década
de 90.
""".replace('\n', ' ')[1:-1],
    '1917'),
    ('Intrinseca',
"""
Intrínseca é uma editora brasileira, responsável pela publicação
de diversos livros de ficção e não-ficção no país. Atualmente,
é uma das cinco maiores editoras do Brasil, considerando o número
de livros vendidos. A Intrínseca publica, em média, 30 livros por ano.
""".replace('\n', ' ')[1:-1],
    '2003'),
    ('Companhia das Letra',
"""
A Companhia das Letras é a maior editora localizada no Brasil,
fundada em 1986, com sede em São Paulo.
""".replace('\n', ' ')[1:-1],
    '1986')
]

for i in editoras:
    u = Banco.Editora(*i)
    u.inserirObjeto()

print("Editoras:")
exibir = Banco.Editora()
exibir.buscarTodosObjetos()
print()

# class Genero:
#     def __init__(self, idGenero=None, nome=None)

generos = [
    ('Fantasia',),
    ('Ficcao',),
    ('Romance',),
    ('Nao-ficcao',),
    ('Classicos',)
]

for i in generos:
    u = Banco.Genero(*i)
    u.inserirObjeto()

print("Generos:")
exibir = Banco.Genero()
exibir.buscarTodosObjetos()
print()

# class Livro:
#     def __init__(self, nome=None, rating_media=None,
#                 capa=None, data_publicacao=None, sinopse=None,
#                 idAutor=None, idEditora=None, idGenero=None)

capas = [
    'capas/alienista.jpg', 'capas/alquimista.jpg',
    'capas/antropoceno-notas-sobre-a-vida-na-terra.jpg',
    'capas/dom_casmurro.jpg', 'capas/harry_potter_pedra_filosofal.jpg',
    'capas/orgulho_preconceito.jpg', 'capas/pessoas_normais.jpg'
]

livros = [
    ('Harry Potter e a Pedra Filosofal', 3.2,
    imagemParaBinario(capas[4]), '1997-06-26',
"""
Harry Potter é um garoto cujos pais, feiticeiros, foram
assassinados por um poderosíssimo bruxo quando ele ainda
era um bebê. Ele foi levado, então, para a casa dos tios
que nada tinham a ver com o sobrenatural. Pelo contrário.
Até os 10 anos, Harry foi uma espécie de gata borralheira:
maltratado pelos tios, herdava roupas velhas do primo gorducho,
tinha óculos remendados e era tratado como um estorvo. No
dia de seu aniversário de 11 anos, entretanto, ele parece deslizar
por um buraco sem fundo, como o de Alice no país das maravilhas,
que o conduz a um mundo mágico.
""".replace('\n', ' ')[1:-1],
    3, 2, 1),
    ('O Alienista', 4.7, imagemParaBinario(capas[0]), '1882-03-15',
"""
Médico, Simão Bacamarte passa a se interessar pela psiquiatria,
iniciando um estudo sobre a loucura em Itaguaí, onde funda a Casa
Verde - um típico hospício oitocentista -, arregimentando cobaias
humanas para seus experimentos. O que se segue é uma história
surpreendente e atual em seu debate sobre desvios e normalidade,
loucura e razão.
""".replace('\n', ' ')[1:-1],
    1, 1, 5),
    ('Dom Casmurro', 4.4, imagemParaBinario(capas[3]), '1899-04-25',
"""
Dom Casmurro é a alcunha de Bento Santiago, que, velho e só,
desvela as suas memórias. Uma promessa da mãe, traça-lhe o
destino como padre, mas Bento Santiago apaixonado, abandona o
seminário. Estuda Direito e casa-se com o seu grande amor, mas
o ciúme e a desconfiança adensam-se. Suspeita que não é o pai
biológico do filho do casal, Ezequiel, mas sim o seu grande amigo
Escobar.
""".replace('\n', ' ')[1:-1],
    1, 3, 5),
    ('Pessoas Normais', 3.85, imagemParaBinario(capas[6]),
    '2018-08-28',
"""
Ele é a estrela do time de futebol, ela é solitária e preza por
sua privacidade. A mãe de Connell trabalha como empregada na casa
dos pais de Marianne, e quando o garoto vai buscar a mãe depois do
expediente, uma conexão estranha e indelével cresce entre os dois
adolescentes.
""".replace('\n', ' ')[1:-1],
    2, 5, 3),
    ('Antropoceno: Notas Sobre a Vida na Terra', 4.0,
    imagemParaBinario(capas[2]), '2021-05-18',
"""
Em seu primeiro livro de não ficção, o premiado autor de A culpa
é das Estrelas analisa as contradições e as maravilhas da humanidade
que John Green é um dos autores contemporâneos mais queridos não é
novidade. Sua sensibilidade e seu talento para traçar histórias
inesquecíveis tornaram seus romances sucessos mundiais, e agora o
celebrado escritor nos oferece uma necessária dose de esperança em
sua estreia na não ficção. Refletindo sobre temas que vão de Super
Mario Kart e o pôr do sol a pinturas rupestres e o hábito de procurar
estranhos no Google, os ensaios perspicazes e bem-humorados reunidos
nesta coletânea são uma celebração genuína da capacidade humana de se
apaixonar pelo mundo.
""".replace('\n', ' ')[1:-1],
    4, 5, 4),
    ('O Alquimista', 3.9, imagemParaBinario(capas[1]), '1988-08-14',
"""
O Alquimista é a história de um jovem que tem um sonho repetido com
um tesouro oculto guardado perto das pirâmides do Egipto. Este resolve
seguir o seu sonho, enfrenta as maiores dificuldades, atravessa desertos
e defronta-se com os grandes mistérios que acompanham o Homem desde o
começo dos tempos: os sinais de Deus, a Lenda Pessoal que cada um de
nós tem que viver, a misteriosa Alma do Mundo, onde qualquer pessoa
pode penetrar se ouvir a voz do seu coração.
""".replace('\n', ' ')[1:-1],
    6, 4, 2),
    ('Orgulho e Preconceito', 4.1, imagemParaBinario(capas[5]), '1813-01-28',
"""
Orgulho e preconceito é o livro mais famoso de Jane Austen e possui
uma série de personagens inesquecíveis e um enredo memorável. Austen nos
apresenta Elizabeth Bennet como heroína irresistível e seu pretendente
aristocrático, o sr. Darcy. Nesse livro, aspectos diferentes são abordados:
orgulho encontra preconceito, ascendência social confronta desprezo social,
equívocos e julgamentos antecipados conduzem alguns personagens ao sofrimento
e ao escândalo. O livro pode ser considerado a obra-prima da escritora,
que equilibra comédia com seriedade, observação meticulosa das atitudes
humanas e sua ironia refinada. A nova coleção possui capa dura e estilo
inspirado nos bullet journals.
""".replace('\n', ' ')[1:-1],
    5, 5, 3)
]

print("Adicionando livros...")

for i in livros:
    u = Banco.Livro(*i)
    u.inserirObjeto()

# class Review:
#     def __init__(self, conteudo=None, data_postagem=None,
#                 rating=None, idLivro=None, idUsuario=None)

reviews = [
    (
"""
Não há palavras para fazer justiça a este livro.
""".replace('\n', ' ')[1:-1], '2013-03-06', 5, 1, 1
    ),
    (
"""
uau. um dos livros mais frustrantes, mas humanizadores, que li em
muito tempo. claro que sim. eu me sinto tão exausto depois de ler
isso, mas acho que pode ter sido a intenção do autor. isso mostra
que pessoas normais vivendo vidas normais podem ser bastante cansativas.
por exemplo: a escrita não tem aspas, o que dificulta a decifração do
diálogo. o que poderia ser visto como suporte para a ideia de que a vida
é tão confusa quanto a formatação e comunicação dos livros às vezes exige
esforço para entender. há grandes saltos na linha do tempo com muito retrocesso,
tanto que as mudanças drásticas são chocantes. o que pode ser visto como um
exemplo da noção de que as pessoas mudam ao longo do tempo e as amizades estão
fadadas a mudar. coisas como esta irão polarizar os leitores. ou é demais e
desagradável, ou é um trabalho de gênio e adiciona profundidade à narrativa.
eu acho que realmente depende da interpretação e humor dos leitores. e como a
criatura indecisa que sou, estou bastante dividida ao meio.
""".replace('\n', ' ')[1:-1], '2019-04-29', 3, 4, 5
    ),
    (
"""
"Quando você realmente quer algo, todo o universo conspira para ajudá-lo a
alcançá-lo" .Este livro ultrapassou as fronteiras dos livros e ganhou vida própria,
criando um movimento em todo o mundo. A jornada e busca espiritual de Santiago,
as pessoas que ele conhece, os sonhos que ele tem, os presságios que ele encontra
e a natureza com a qual ele fala, são todas as coisas com as quais podemos nos relacionar...
coisas que esquecemos ou simplesmente descartamos como fantasias infantis. Trata-se de
encontrar sua lenda pessoal e perseguir seu sonho, independentemente de quaisquer obstáculos,
e de estar espiritualmente conectado ao universo, que é parte de nós e parte de Deus. Nós
somos todos um. Ler este livro sempre me coloca de volta no caminho certo para alcançar os sonhos
que adiei. Nós sempre tentamos fazer o que todos esperam de nós, como seguir uma carreira que
você odeia só porque é isso que todos fazem. Reconhecer minha lenda pessoal, poder falar com as
árvores, o céu, as formigas, o núcleo da terra, as partículas de ar e com o meu coração,
sentindo uma conexão espiritual mais profunda com tudo/todos que estão ao meu redor, sentindo Deus
dentro de mim , e não ter medo de falhar ou enfrentar desafios são apenas algumas das poucas coisas
que este livro me deu. É maktub que Coelho escreve este livro, compartilha com o mundo e afeta
tantas vidas. Esta obra-prima é uma lenda e um tesouro precioso
""".replace('\n', ' ')[1:-1], '2008-08-19', 5, 6, 3
    ),
    (
"""
O mais intrigante em Dom Casmurro, de Machado de Assis, é a forma como o narrador o
convida para o seu mundo e as partes íntimas de sua vida, os episódios que ele julgou
formarem quem ele se tornaria mais tarde. Mesmo quando ele está relatando algumas de
suas lutas ao crescer ou fornecendo antecedentes a membros importantes da família, o
tom é de aceitação silenciosa, distanciamento filosófico e até humor. Quando o leitor
chega às últimas 40 ou 50 páginas e percebe que tudo até então foi escrito como uma
armação para a conclusão, Dom Casmurro torna-se notável e trágico. Este é um romance
emocionante. Pretendo ler mais da obra deste autor brasileiro.
""".replace('\n', ' ')[1:-1], '2019-10-06', 4, 3, 1
    ),
    (
"""
Uma coletânea de ensaios sobre as coisas mais aleatórias: condicionadores de ar (essa
eu realmente gostei muito), barracas de cachorro-quente, gansos do Canadá, aplicativo
de notas, etc (que eu realmente não me importei). Parecia uma estranha mistura de informações
factuais misturadas com experiências pessoais. Eu não categorizo ​​adequadamente isso
como uma não-ficção informativa ou um livro de memórias. John Green usa tantas citações
(as de Kurt Vonnegut que eu adorei, mas prefiro apenas ler algo de Kurt Vonnegut) e,
portanto, parecia que eu estava lendo uma coleção do que outros disseram - resultando
em uma experiência de leitura genérica. Eu também posso ter superado John Green, não me
importando muito com suas opiniões (desculpe). Eu realmente tive que me forçar a passar
por isso, e se não fosse pela versão do audiolivro eu poderia não ter terminado. Dou 2
estrelas a este livro.
""".replace('\n', ' ')[1:-1], '2021-11-27', 2, 5, 2
    )
]

for i in reviews:
    u = Banco.Review(*i)
    u.inserirObjeto()

print("Reviews:")
exibir = Banco.Review()
exibir.buscarTodosObjetos()
print()

# class Lista:
#     def __init__(self, idUsuario=None,
#                 nome=None, descricao=None):

listas = [
    (5, 'Os Melhores de 2021', 'meus favoritos de 2021'),
    (5, 'Leituras da Pandemia', 'Livros que li durante o isolamento'),
    (3, 'Livros que li na infancia', None),
    (1, 'minha mae me indicou', 'livros q minha mae mandou ler'),
    (2, 'me ajudaram a crescer', None)
]

for i in listas:
    u = Banco.Lista(*i)
    u.inserirObjeto()

print("Listas:")
exibir = Banco.Lista()
exibir.buscarTodosObjetos()
print()

# class Lista_has_Livro:
#     def __init__(self, idLista=None, idLivro=None)

listas_h_livro = [
    (5, 4),
    (5, 5),
    (5, 6),
    (1, 5),
    (2, 2),
    (2, 7),
    (2, 3),
    (3, 1),
    (3, 2),
    (3, 3),
    (4, 2),
    (4, 3),
    (4, 6)
]

for i in listas_h_livro:
    u = Banco.Lista_has_Livro(*i)
    u.inserirObjeto()

print("Lista has Livros:")
exibir = Banco.Lista_has_Livro()
exibir.buscarTodosObjetos()
print()

# class Lido:
#     def __init__(self, idUsuario=None)

lidos = [
    (1,),
    (2,),
    (3,),
    (4,),
    (5,)
]

for i in lidos:
    u = Banco.Lido(*i)
    u.inserirObjeto()

exibir = Banco.Lido()
exibir.buscarTodosObjetos()
print()

# class Lido_has_Livro:
#     def __init__(self, idUsuario=None, idLivro=None)

lidos_h_livro = [
    (1, 1),
    (1, 3),
    (5, 7),
    (5, 4),
    (5, 2),
    (2, 5),
    (3, 6),
    (3, 7),
    (4, 5)
]

for i in lidos_h_livro:
    u = Banco.Lido_has_Livro(*i)
    u.inserirObjeto()

print("Lido Has Livro:")
exibir = Banco.Lido_has_Livro()
exibir.buscarTodosObjetos()
print()

# class Lendo:
#     def __init__(self, idUsuario=None)

lendos = [
    (1,),
    (2,),
    (3,),
    (4,),
    (5,)
]

for i in lendos:
    u = Banco.Lendo(*i)
    u.inserirObjeto()

print("Lendo:")
exibir = Banco.Lendo()
exibir.buscarTodosObjetos()
print()

# class Lendo_has_Livro:
#     def __init__(self, idUsuario=None, idLivro=None)

lendo_h_livro = [
    (1, 2),
    (2, 1),
    (2, 2),
    (3, 4),
    (4, 3),
    (5, 6)
]

for i in lendo_h_livro:
    u = Banco.Lendo_has_Livro(*i)
    u.inserirObjeto()

print("Lendo Has Livro:")
exibir = Banco.Lendo_has_Livro()
exibir.buscarTodosObjetos()
print()

# class QueroLer:
#     def __init__(self, idUsuario=None)

quero_ler = [
    (1,),
    (2,),
    (3,),
    (4,),
    (5,)
]

for i in quero_ler:
    u = Banco.QueroLer(*i)
    u.inserirObjeto()

print("Quero Ler:")
exibir = Banco.QueroLer()
exibir.buscarTodosObjetos()
print()

# class QueroLer_has_Livro:
#     def __init__(self, idUsuario=None, idLivro=None)

quero_ler_h_livro = [
    (1, 4),
    (1, 5),
    (2, 3),
    (3, 5),
    (3, 2),
    (4, 6),
    (5, 1),
    (5, 3),
    (5, 5)
]

for i in quero_ler_h_livro:
    u = Banco.QueroLer_has_Livro(*i)
    u.inserirObjeto()

print("Quero Ler Has Livro:")
exibir = Banco.QueroLer_has_Livro()
exibir.buscarTodosObjetos()
print()