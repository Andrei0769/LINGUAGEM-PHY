import os

os.system("cls || clear")

class Livro:
    def __init__(self, titulo, autor, num_paginas, preco):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        self.preco = preco

num_livros = int(input("Quantos livros você deseja cadastrar? "))

livros = []
for i in range(num_livros):
    print(f"\nDados do livro {i+1}:")
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    num_paginas = int(input("Digite o número de páginas do livro: "))
    preco = float(input("Digite o preço do livro: "))
    
    livros.append(Livro(titulo, autor, num_paginas, preco))

print("\nDetalhes dos livros cadastrados:")
for i, livro in enumerate(livros):
    print(f"\nLivro {i+1}:")
    print("Título:", livro.titulo)
    print("Autor:", livro.autor)
    print("Número de páginas:", livro.num_paginas)
    print("Preço:", livro.preco)
