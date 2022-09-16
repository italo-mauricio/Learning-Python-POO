
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
        
p1 = Pessoa.por_ano_nascimento('Italo', 1998)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()