"""
Card class: #TODO list:
1. values (power)
2. names (clans, power-ups idk)
"""
import random

ranks = {
    'Dweller':1,
    'Farmer':2,
    'Engineer':3,
    'Miner':4,
    'Blacksmith':5,
    'Alchemist':6,
    'Fighter':7,
    'Knight':8,
    'Priest':9,
    'Lord':10,
    'King':11,
    'Queen':12,
    'Creator':13
}


clans = ('Dark Ages', 'Edo Shogunate', 'Kahuna Papyrus', 'Cicada')

names = ('Shantae', 'Kirigaya', 'Albedo', 'Lyhoman', 'Star', 'Shrimp', 'Shfart', 'Joji', 'Gura', 'Ame', 'Ken', 'Kuro', 'Shiro', 'Shinji', 'Paimon', 'Tharja', 'Darling', 'Arararagi', 'Rickrolled', 'Toradora', 'Big tiddie gf', 'Smol tiddie goth gf', 'Ricardo', 'Spongebob', 'Bo Burnham', 'Monika', 'Padowu Padowu', 'Scooby-Doo', 'AppleJack', 'Based', 'Bahh Tee', 'Sportacus', 'Asuka')


class Card():

    def __init__(self, name, clan, rank):
        self.name = name
        self.clan = clan
        self.value = ranks[rank]

    def __str__(self):
        return f'{self.name} | CLAN: {self.clan} | VALUE: {self.value}'
    
    def __len__(self):
        return self.value
