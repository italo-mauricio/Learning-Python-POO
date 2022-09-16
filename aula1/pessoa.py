from mailbox import NotEmptyError


class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade  
              
        
        
        
    def falar(self):
        print(f'{self.nome} esta falando...')
        
        
        

# self