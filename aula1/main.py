from pessoa import Pessoa



# Aula sobre Classes



p2 = Pessoa ('pedro', 23 , 2022)
p3 = Pessoa ('italo', 24, 2022)
#p2.anothermethod()
#p2.comer('arroz')
#p2.falar('POO')
#p2.parar_comer()
#p2.falar('POO')
#p2.comer('feijão')
#p2.parar_comer()
#p2.falar('assunto')

p2.falar('POO')
p3.falar('filmes')
p2.comer('Churrasco')
print(f'{p2.nome} nasceu em', p2.ano_nascimento())
print(f'{p3.nome} nasceu em', p3.ano_nascimento())
