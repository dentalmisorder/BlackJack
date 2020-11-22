"""
START POINT FOR THE GAME! SETTINGS/SETUP IS BELOW!

LAUNCH THE GAME FROM THIS FILE PLEASE :)
"""
#=============LIBRARIES==============

import deck
import card
import hand
import random
import os
from colorama import init
from colorama import deinit
from colorama import Fore
init(autoreset=True)

#==============SETUP/SETTINGS=============

player_input = ''           #to start a while loop for drawing cards
started_bank_amount = 500   #amount of money that everyone will have at the start
game_over_points = 21       #if someone will have more then that == game over
blackjack = True            #is the game start at the start or not
game_on = False              
game_round = 1              #basically what it says
player_turn = True          #can player choose draw or skip?
dealer_turn = True          #can dealer choose draw or skip?
is_bet_avaliable = True     #can player/dealer bet money at the start?

player = hand.Hand(started_bank_amount)
dealer = hand.Hand(started_bank_amount)

player_bet = 0
dealer_bet = 0

#================METHODS================

def setup_for_next_round(game_round):
    print(f'\n\tROUND [{game_round}]')
    print(f'\tPLAYER BANK:{Fore.GREEN} {player.bank_amount}$')
    print(f'\tDEALER BANK:{Fore.RED} {dealer.bank_amount}$\n')
            
    new_deck = deck.Deck()      #creating a new deck with cards
    player.clear_hand()         #clearing hands for new cards
    dealer.clear_hand()         #in case if its more then first round

    #player starts with 2 cards and dealer 1 card and 1 down
    #we will reveal this card at the start of first turn
    player.add_card(new_deck.take_one())
    player.add_card(new_deck.take_one())
    dealer.add_card(new_deck.take_one())

    return new_deck

def show_all_cards():
    for key,value in card.ranks.items():
        print(f'CARD NAME: {key} | CARD RANK (value): {value}')
    print(f'Detailed info about cards, perks and the developer here:\n{Fore.MAGENTA}https://github.com/doulikedarkness/BlackJack')

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def draw_started_cards():
    print("""
    DEALER CARDS:
    """)
    for cards in dealer.hand_cards:
        print(cards)

    print(f'\n{Fore.RED} TOTAL VALUE DEALER CARDS: {dealer.value}\n')

    print("""
    PLAYER CARDS:
    """)
    for cards in player.hand_cards:
        print(cards)
    
    print(f'\n{Fore.RED} TOTAL VALUE PLAYER CARDS: {player.value}\n')

def check_for_money(blackjack):
    if player.bank_amount <= 0:
        print(Fore.MAGENTA+'Player is a bankrupt!')
        return False
    elif dealer.bank_amount <= 0:
        print(Fore.MAGENTA+'Dealer is bankrupt!')
        return False
    else:
        return True

def bet(is_bet_avaliable):
    while is_bet_avaliable:
            try:
                player_bet = int(input(f'Place a bet ({player.bank_amount}$): '))
            except:
                print(Fore.MAGENTA+'Type in your bet!')
            else:
                if player_bet > 0 and player_bet <= player.bank_amount:
                    dealer_bet = random.choice(range(dealer.bank_amount))

                    player.bet_amount(player_bet)
                    dealer.bet_amount(dealer_bet)
                                        
                    print(f'Dealer placed a bet for {Fore.RED} {dealer_bet}$')
                    print(f'You placed a bet for {Fore.GREEN} {player_bet}$')
                    break
                else:
                    print(Fore.MAGENTA+'Place a bet that you can afford...')

def player_take_cards(player_turn, dealer_turn, player_input, game_on):
    if player_turn: 
        if player.value < game_over_points:
            
            while 'DRAW' not in player_input.upper() or 'SKIP' not in player_input.upper():
                player_input = input('Are you DRAW a card or SKIP?: ')
                if 'DRAW' in player_input.upper():
                    print('=========================================')
                    new_card = new_deck.take_one()
                    player.add_card(new_card)
                    print(f'You took a card: {new_card}')
                    print(f'TOTAL VALUE OF YOUR CARDS NOW: {player.value}')
                    print('=========================================')
                    if player.value > game_over_points:
                        print(f'YOU LOSE WITH TOTAL VALUE OF {player.value} AND WITH {len(player.hand_cards)} CARDS IN HAND!')
                        return False
                elif 'SKIP' in player_input.upper():
                    return True

def dealer_take_cards(dealer_turn):
    if dealer_turn:
        print('=========================================')
        new_card = new_deck.take_one()
        dealer.add_card(new_deck.take_one())
        print(f'Dealer opens the seconds card.. {new_card}')
        print(f'DEALER TOTAL VALUE NOW: {dealer.value}')

        if dealer.value < game_over_points:
            while dealer.value < (game_over_points - 6):
                new_card = new_deck.take_one()
                dealer.add_card(new_card)
                print(f'Dealer took a card: {new_card}')
                print(f'DEALER TOTAL VALUE: {dealer.value}')
            print('=========================================')

def check_results(player, dealer, game_on):
    if game_on:
            if dealer.value > game_over_points and player.value < game_over_points:
                player.won_bet(dealer.amount_betted)
                print(f'DEALER HAS TOTAL VALUE OF {dealer.value}, HE LOSE! PLAYER WINS!')
                print(f'Player got {Fore.GREEN} {dealer.amount_betted}$ ({player.bank_amount})')

            elif player.value > game_over_points and dealer.value < game_over_points:
                dealer.won_bet(player.amount_betted)
                print(f'PLAYER HAS TOTAL VALUE OF {player.value}, HE LOSE! DEALER WINS!')
                print(f'Dealer got {Fore.RED} {player.amount_betted}$ ({dealer.bank_amount})')

            elif player.value > dealer.value:
                player.won_bet(dealer.amount_betted)
                print(f'PLAYER HAS TOTAL VALUE OF {player.value}, MORE THEN DEALER WITH {dealer.value}, PLAYER WINS!')
                print(f'Player got {Fore.GREEN} {dealer.amount_betted}$ ({player.bank_amount})')

            elif dealer.value > player.value:
                dealer.won_bet(player.amount_betted)
                print(f'DEALER HAS TOTAL VALUE OF {dealer.value}, MORE THEN PLAYER WITH {player.value}, DEALER WINS!')
                print(f'Dealer got {Fore.RED} {player.amount_betted}$ ({dealer.bank_amount})')
            
            elif dealer.value == player.value:
                dealer.won_bet()
                player.won_bet()
                print(f'TIE! PLAYER GOT {player.value} AND DEALER GOT {dealer.value}')

#==================GAME====================
if __name__ == '__main__':
    while blackjack:
        clear() #clear the console
        print(f"""
        [WELCOME, CHOOSE A TABLE, SIT AND RELAX]
        [COMMANDS: [START], [CARDS]]

        [ALL CARDS AND THEIR PERKS COULD BE FOUND HERE:]
        {Fore.MAGENTA} [https://github.com/doulikedarkness/BlackJack]
        """)
        bj_input = input('Wanna start a game?: ')
        if 'START' in bj_input.upper() or 'YES' in bj_input.upper():
            blackjack = False
            game_on = True
        elif 'CARDS' in bj_input.upper():
            game_on = False
            show_all_cards()


        while check_for_money(blackjack) and game_on:
            new_deck = setup_for_next_round(game_round)

            check_for_money(blackjack)
            bet(is_bet_avaliable)
            draw_started_cards()
                
            #if at that point player fails dealer isnt goin and game also stops
            result = player_take_cards(player_turn, dealer_turn, player_input, game_on)
            dealer_turn = result

            dealer_take_cards(dealer_turn)

            #check results if game wasnt ended while both took cards
            check_results(player, dealer, game_on)
            game_round += 1
        
else:
    print(f'{Fore.RED} YOU NEED TO LAUNCH game.py INSTEAD OF ANYTHING ELSE')
    print(f'{Fore.MAGENTA} If you get this error while trying to launch game.py remove line contains: if __name__ == "__main__":')

deinit()
