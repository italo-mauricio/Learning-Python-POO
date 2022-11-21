from pessoa import Pessoa


p1 = Pessoa('bananinha','23')
p2 = Pessoa('lucas', '45')
p3 = Pessoa('italo', '44')


p1.falar()
p2.falar()
p3.falar()

print(p2.vivo)
p2.morrer()
print(p2.vivo)

p3.comendo()
print(p3.comendo)