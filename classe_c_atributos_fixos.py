## O método construtor __init__ ele constroi os atributos para uma instancia
# O self/namespace são os valores atribuidos e exclusivos para cada
# Atributo de um objeto


class livro():
    def __init__(self):
        self.autor = "Arthur Faral"
        self.titulo = "O curso"
    
    #agora não é mais uma função e sim um metodo por estar dentro da classe/ação
    def imprime(self):
        print("Esse livro é do %s e o Autor %s"%(self.titulo,self.autor))



## Instanciar os objetos 

livro1 = livro()

## Listar os atributos do objeto

print(livro1.titulo)
print(livro1.autor)

livro1.imprime()


