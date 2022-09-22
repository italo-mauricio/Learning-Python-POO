# Métodos Getters e Setters


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco *(percentual / 100))
        
    # Getter
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,valor):
        self._nome = valor
    
    
    @property
    def preco(self):
        return self._preco
    
    # Setter
    
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
            
            
        self._preco = valor
        
        
        
p1 = Produto('camisa', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('sapato', 'R$15') # o replace pode dar conflito se alterar essa sring adicionando espaços, ou pontos
p2.desconto(10)
print(p2.nome, p2.preco)