import random
from function_pkg.user import war

#deck is 52 cards without the jokers, suites don't matter, aces are high
deck = ["A","2","3","4","5","6","7","8","9","10","J","Q","K","A","2","3","4","5","6","7","8","9","10","J","Q","K","A","2","3","4","5","6","7","8","9","10","J","Q","K","A","2","3","4","5","6","7","8","9","10","J","Q","K"] 
player_1 = []
player_2 = []

while True:
    first_card_chosen = [0]
    second_card_chosen = [0]
    card = input("Each player pick a card, or press Q then enter to quit ")
    if card == "Q":
        break
    if not deck:
        print("There are no more cards to pick.")
        break
    else: 
        random.shuffle(deck)
        player_1.extend(random.sample(deck, 26))
        player_2.extend(random.sample(deck, 26))
        first_card_chosen = random.choice(player_1) 
        second_card_chosen = random.choice(player_2)
        player_1.remove(first_card_chosen)
        player_2.remove(second_card_chosen)
        if first_card_chosen == second_card_chosen:
            print("\n------------------------------------------------------------------------THERE IS WARR!----------------------------------------------------------\n")
            war(player_1, player_2)
        print("\nPlayer 1 draws ",first_card_chosen)
        print("Player 2 draws ",second_card_chosen)
        print("\n------------------------------------------------------------------------Remaining Cards----------------------------------------------------------\n")
        print("\nplayer 1: ", player_1) 
        print("player 2: ", player_2) 

"""
Game Instructions
1) The objective of the game is to win all of the cards.
2) The deck is divided evenly among the players 
3) In unison, each player reveals the top card of their deck—this is a "battle"
4) player with the higher card takes both of the cards played and moves them to their stack.
5) Aces are high, and suits are ignored.
6) If the two cards played are of equal value, then there is a "war".
7) Both players place the next three cards face down and then another card face-up.
Finishing current step: 
8) The owner of the higher face-up card wins the war and adds all the cards on the table to the bottom of their deck.
9) If the face-up cards are again equal then the battle repeats with another set of face-down/up cards. This repeats until one player's face-up card is higher than their opponent's.
10) Ask the player if they want to play again. 
11) Quit if they say no, and start from the beginning if they say yes. 

"""        


    
