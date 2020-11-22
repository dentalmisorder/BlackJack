import card

class Hand():

    def __init__(self, bank_amount):
        self.bank_amount = bank_amount
        self.hand_cards = []
        self.value = 0
        self.amount_betted = 0

    def add_card(self, cards):
        if type(cards) == []:
            for c in cards:
                self.hand_cards.append(c)
                self.value = self.value + c.value
        else:
            self.hand_cards.append(cards)
            self.value = self.value + cards.value
    
    def clear_hand(self):
        self.hand_cards.clear()
        self.value = 0

    def bet_amount(self, amount):
        if amount <= self.bank_amount:
            self.amount_betted = amount
            self.bank_amount -= amount
        
    def won_bet(self, *other_players_bets):
        self.bank_amount += self.amount_betted + sum(other_players_bets)

    def __str__(self):
        return f'{self.hand_cards} cards in hand with total value {self.value}, and {self.bank_amount}$ in bank account'
