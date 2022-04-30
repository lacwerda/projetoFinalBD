create database projeto_final;
use projeto_final;

create table Usuario (
idUsuario INT primary key auto_increment,
username VARCHAR(20) not null unique,
nome VARCHAR(45) not null,
bio VARCHAR(300),
cidade VARCHAR(45),
pais VARCHAR(45)
);

create table Autor (
idAutor INT primary key auto_increment,
nomeAutor VARCHAR(45) not null,
biografia VARCHAR(1000),
website VARCHAR(300),
twitter VARCHAR(45),
data_nascimento DATE
);

create table Editora (
idEditora INT primary key auto_increment,
nomeEditora VARCHAR(45) not null,
sobre VARCHAR(400),
ano_fundacao YEAR
);

create table Genero (
idGenero INT primary key auto_increment,
nomeGenero VARCHAR(45)
);

create table Livro (
idLivro INT primary key auto_increment,
nomeLivro VARCHAR(200) not null,
rating_media FLOAT not null,
capa LONGBLOB, # IMAGEM EM VALOR BINARIO
data_publicacao DATE not null,
sinopse VARCHAR(1000),
idAutor INT not null,
idEditora INT not null,
idGenero INT not null,
FOREIGN KEY (idAutor) REFERENCES Autor(idAutor) ON DELETE CASCADE,
FOREIGN KEY (idEditora) REFERENCES Editora(idEditora) ON DELETE CASCADE,
FOREIGN KEY (idGenero) REFERENCES Genero(idGenero) ON DELETE CASCADE
);

create table Review (
idReview INT primary key auto_increment,
conteudo VARCHAR(2000) not null,
data_postagem DATE not null,
rating INT,
idLivro INT not null,
idUsuario INT not null,
FOREIGN KEY (idLivro) REFERENCES Livro(idLivro) ON DELETE CASCADE,
FOREIGN KEY (idUsuario) REFERENCES Usuario(idUsuario) ON DELETE CASCADE
);

create table Lista (
idLista INT primary key auto_increment,
idUsuario INT not null,
nome VARCHAR(100) not null,
descricao VARCHAR(200),
FOREIGN KEY (idUsuario) REFERENCES Usuario(idUsuario) ON DELETE CASCADE
);

create table Lista_has_Livro (
idLista INT not null,
idLivro INT not null,
FOREIGN KEY (idLista) REFERENCES Lista(idLista) ON DELETE CASCADE,
FOREIGN KEY (idLivro) REFERENCES Livro(idLivro) ON DELETE CASCADE
);

create table Lido (
idUsuario INT primary key,
FOREIGN KEY (idUsuario) REFERENCES Usuario(idUsuario) ON DELETE CASCADE
);

create table Lido_has_Livro (
idUsuario INT not null,
idLivro INT not null,
FOREIGN KEY (idUsuario) REFERENCES Lido(idUsuario) ON DELETE CASCADE,
FOREIGN KEY (idLivro) REFERENCES Livro(idLivro) ON DELETE CASCADE
);

create table Lendo (
idUsuario INT primary key,
FOREIGN KEY (idUsuario) REFERENCES Usuario(idUsuario) ON DELETE CASCADE
);

create table Lendo_has_Livro (
idUsuario INT not null,
idLivro INT not null,
FOREIGN KEY (idUsuario) REFERENCES Lendo(idUsuario) ON DELETE CASCADE,
FOREIGN KEY (idLivro) REFERENCES Livro(idLivro) ON DELETE CASCADE
);

create table QueroLer (
idUsuario INT primary key,
FOREIGN KEY (idUsuario) REFERENCES Usuario(idUsuario) ON DELETE CASCADE
);

create table QueroLer_has_Livro (
idUsuario INT not null,
idLivro INT not null,
FOREIGN KEY (idUsuario) REFERENCES QueroLer(idUsuario) ON DELETE CASCADE,
FOREIGN KEY (idLivro) REFERENCES Livro(idLivro) ON DELETE CASCADE
);