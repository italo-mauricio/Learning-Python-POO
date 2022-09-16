class Pessoa:
    def __init__(self,nome, idade, ano, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.ano = ano  
        self.comendo = comendo
        self.falando = falando

        
    
    def anothermethod(self):
        print(f'O ano é {self.ano}')
        print(f'ele se chama {self.nome}')
        print(f'e tem {self.idade} anos')

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True
        
        
    
         
          
        