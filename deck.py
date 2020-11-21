import card
import random

class Deck():

    def __init__(self):
        self.all_cards = []

        for clan in card.clans:
            for rank in card.ranks:
                new_card = card.Card(rank, clan, rank)
                self.all_cards.append(new_card)
        random.shuffle(self.all_cards) #shuffles created deck

    def __len__(self):
        return len(self.all_cards)
    
    def __str__(self):
        return f'Deck has {len(self.all_cards)} cards'

    def take_one(self):
        return self.all_cards.pop()
    