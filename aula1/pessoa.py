class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando 
        
        
    def anothermethod(self):
        print(f'ele se chama {self.nome}')
        print(f'e tem {self.idade} anos')

    def comer(self, alimento):
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True
         
          
        