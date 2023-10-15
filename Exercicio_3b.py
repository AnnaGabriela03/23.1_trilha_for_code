# literalmente uma biblioteca no python
class Livro:
    def __init__(self, titulo, autor, codigo):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        else:
            return False

    def devolver(self):
        self.disponivel = True

    def __str__(self):
        disponibilidade = "Disponível" if self.disponivel else "Indisponível"
        return f"{self.titulo} por {self.autor} (ISBN: {self.codigo}) - {disponibilidade}"


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def procurar_livro(self, codigo):
        for livro in self.livros:
            if livro.codigo == codigo:
                return livro
        return None

    def __str__(self):
        if not self.livros:
            return "A biblioteca está vazia."
        else:
            lista_livros = "\n".join(str(livro) for livro in self.livros)
            return f"Livros na biblioteca:\n{lista_livros}"


class Usuario:
    def __init__(self, nome):
        self.nome = nome

    def emprestar_livro(self, livro, biblioteca):
        if livro.emprestar():
            print(f"{self.nome} pegou emprestado o livro: {livro.titulo}")
        else:
            print(f"O livro {livro.titulo} não está disponível para empréstimo.")

    def devolver_livro(self, livro, biblioteca):
        livro.devolver()
        print(f"{self.nome} devolveu o livro: {livro.titulo}")


if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Da pra melhorar
    livro1 = Livro("livro 1", "Autor 1", "123-356")
    livro2 = Livro("livro 2", "Autor 2", "789-123")

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    usuario1 = Usuario("Joaquim")
    usuario2 = Usuario("Maria")

    print(biblioteca)

    usuario1.emprestar_livro(livro1, biblioteca)
    print(biblioteca)

    usuario2.emprestar_livro(livro2, biblioteca)
    print(biblioteca)

    usuario1.devolver_livro(livro1, biblioteca)
    print(biblioteca)
