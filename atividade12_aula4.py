class Biblioteca:
    def __init__(self):
         self.library = []

    def adicionarLivros(self, titulo,autor,ano,status):

        livro = Livros(titulo,autor,ano,status)

        if (livro not in self.library):
            self.library.append(livro)
    
    def listarLivros(self):
        for livro in self.library:
            livro.Exibir_Info()
            
            
class Livros():
     def __init__ (self,titulo,autor,ano,status):
        super().__init__(titulo,autor,ano,status)
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.status = status

        def Exibir_Info(self):
             print(f"O título do Livro é {self.titulo}, o seu autor é {self.autor} o seu ano de publicação é {self.ano} a situação do livro é {self.status}")





