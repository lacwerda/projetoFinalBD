use projeto_final;

DELIMITER //

CREATE PROCEDURE ExibicaoListaUsuario()
BEGIN
	CREATE TABLE ExibirLivros AS
		SELECT
			Livro.nomeLivro,
			Autor.nomeAutor,
			Editora.nomeEditora,
			Livro.rating_media,
			Livro.capa,
            Livro.sinopse,
            Genero.nomeGenero
		FROM Livro
		JOIN Autor
			ON Livro.idAutor = Autor.idAutor
		JOIN Editora
			ON Livro.idEditora = Editora.idEditora
		JOIN Genero
			ON Livro.idGenero = Genero.idGenero;
END //

DELIMITER ;

CALL ExibicaoListaUsuario();
SELECT * FROM ExibirLivros;