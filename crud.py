from dao import Banco
from datetime import date

# READ
def minhasReviewsDeTalLivro(username, idLivro):
    usuario = Banco.Usuario(username=username)
    id = usuario.buscarPorUsername()
    id = id[0]
    review = Banco.Review(idUsuario=id, idLivro=idLivro)
    l = review.buscarPorLivroUsuario()
    return (l)

minhasReviewsDeTalLivro('sabspx', 4)

# UPDATE
def mudarMinhaReview(idReview, novaReview):
    review = Banco.Review()
    review.setIdReview(idReview)
    l = review.buscarPorChavePrimariaObjeto()
    review = Banco.Review(*l[1:])
    review.setIdReview(l[0])
    review.setConteudo(novaReview)
    review.atualizarObjeto()

mudarMinhaReview(2,
"""
Depois de ler algumas vezes, decidi que gostei sim.
""".replace('\n', ' ')[1:-1]
)

# CREATE
def novaReview(conteudo, idLivro, username, rating=None):
    usuario = Banco.Usuario(username=username)
    id = usuario.buscarPorUsername()
    id = id[0]
    review = Banco.Review(conteudo=conteudo, rating=rating,
                        idLivro=idLivro, idUsuario=id)
    review.setDataPostagem(str(date.today()))
    l = review.inserirObjeto()
    print(f'IdReview: {l}')

    return l

novaReview(
"""
Antes de Sigmund Freud, houve Simão Bacamarte!
""".replace('\n', ' '),
2, 'sabspx', 4
)

def deletarReview(idReview):
    review = Banco.Review()
    review.setIdReview(idReview)
    review.apagarObjeto()

deletarReview(2)