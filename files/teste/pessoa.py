
class Pessoa:
    def __init__(self,nome,idade, vivo=True, comendo=False):
        self.nome = nome
        self.idade = idade  
        self.vivo = vivo  
        self.comendo = comendo
        
        
        
    def falar(self):
        print(f'{self.nome} esta falando...')
        print(f'a pessoa está mora? = {self.vivo}')
        print(f'A pessoa está comendo? = {self.comendo}')
    
    def morrer(self):
        self.vivo = False
    def comer(self):
        self.comendo = False
        
        
        

# self