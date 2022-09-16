
# Aula 2, método de classes

class Pessoa:
    ano_atual = 1999
    
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        
        
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)
        
        
    @classmethod    # método de classe
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento 
        return cls(nome, idade)
        
p1 = Pessoa('Italo', 32)
p2 = Pessoa('Pedro', 23)