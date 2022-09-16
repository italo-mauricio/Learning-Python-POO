class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando 
        
        
    def anothermethod(self):
        print(self.nome)
        print(self.idade)

    def comer(self):
        print(f'{self.nome} está comendo.')
        self.comendo = True
         
          
        