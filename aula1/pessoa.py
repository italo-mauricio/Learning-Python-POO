class Pessoa:
    def __init__(self,nome, idade, ano, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.ano = ano  
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        if self.falando:
            print(f'{self.nome} já está falando')
            return
        
        print(f'{self.nome} esta falando sobre {assunto}')
        self.falando = True
    
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        print(f'{self.nome} parou de falar')
        self.falando = False
    
    def anothermethod(self):
        print(f'O ano é {self.ano}')
        print(f'ele se chama {self.nome}')
        print(f'e tem {self.idade} anos')

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        
        if self.falando:
            print(f'{self.nome} não pode falar comendo ')
            return
        
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True
        
    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo")
            return
    
        print(f'{self.nome} parou de comer')
        self.comendo = False
        
        
    
         
          
        