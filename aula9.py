# class Pokemon:
#     tipo = 'fogo'
#     nature = 'adamant'
#     ivs = '186/510'
#     ataque = 'ember'

#     def __init__(self,tipo,nature):
#         self.tipo = tipo
#         self.nature = nature
    
#     def __str__(self):
#         return'oi'
#     def atacar(self):
#         ('atacando')
#     def dano(self):
#         print('dano recebido')

# Pokemon1 = Pokemon('fogo','adamant')

# print(Pokemon1.tipo)
# print(Pokemon1.nature)

# pokemon2 = Pokemon('agua','mild')

# print(pokemon2.tipo)
# print(pokemon2.nature)

class Personagem:
    vida = 100
    moedas = 0
    nivel = 1
    status = 'betinha'

    def __init__(self,nome,classe,familia):
        self.nome = nome
        self.classe = classe
        self.familia = familia
        self.roletar = roletar

    def dano(self, valor):
        self.vida -= valor
        if (self.vida <= 0):
            print('Joga mal em!{self.valor} de dano e faleceu! \nFaz o L')
        else:
            print('Voce tomou {self.valor} de dano!')

    def money(self, valor):
        self.moedas -= valor
        if (self.moedas <= 0):
            print('procure um emprego')
        else:
            print('Voce ganhou um bonus de 50 reisreis no tigrinho')

    def __str__(self):
        return 'oi'
     
    def ganhar(self):
        ('ganhou!')

    def perder(self):
        ('perdeu')

    roleta1 = roletar('ganhar','perder')

    print(roleta1.ganhar)
    print(roleta1.perdeu)                 
Npc = Personagem('Hideraldo', 'arqueiro', 'igof')
