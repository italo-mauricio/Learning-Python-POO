
class Pessoa:
    def __init__(self,nome,idade, vivo=True):
        self.nome = nome
        self.idade = idade  
        self.vivo = vivo  
        
        
        
    def falar(self):
        print(f'{self.nome} esta falando...')
        print(f'a pessoa está {self.vivo}')
    
    def morrer(self):
        self.vivo = False
        
        
        

# self