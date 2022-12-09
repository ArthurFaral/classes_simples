## iremos declarar uma variavel nos atributos do construtor
# da classe

class livro():


## o que vier antes da ação, sera chumbado e colocado a todos os livros


    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor

    def imprime(self):
        print("Esse livro é %s e o autor %s" %(self.titulo,self.autor))



### instanciando os objetos

livro1 = livro("titulo do livro 1","autor do livro 1") # esse possui 1 self/namespace

livro2 = livro("titulo do livro 2","autor do livro 2") # esse possui outro self/namespace
                                                       # de valores de atributos diferentes


print(livro1.titulo)
print(livro2.titulo)

livro1.imprime()
livro2.imprime()
