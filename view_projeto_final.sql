use projeto_final;

CREATE VIEW ReviewParaUsuario AS
SELECT
	Usuario.nome,
    Usuario.username,
    Livro.nomeLivro,
    Review.rating,
	Review.conteudo,
	Review.data_postagem
FROM Review
JOIN Livro
	ON Review.idLivro = Livro.idLivro
JOIN Usuario
	ON Review.idUsuario = Usuario.idUsuario;
    
SELECT * FROM ReviewParaUsuario;