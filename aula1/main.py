from pessoa import Pessoa


p1 = Pessoa('bananinha','23')
p2 = Pessoa('lucas', '45')


p1.falar()
p2.falar()

print(p2.vivo)
p2.morrer()
print(p2.vivo)
