import random

def war(player_1, player_2):
    if player_1.count() and player_2.count() > 4:
        face_down_cards_1 = random.sample(player_1, 3) 
        face_down_cards_2 = random.sample(player_2, 3)
        fir_card_chosen = random.choice(player_1) 
        sec_card_chosen = random.choice(player_2)
        print("Each of you have put 3 cards facedown for the pot!")
        print("\nPlayer 1 draws ",fir_card_chosen)
        print("Player 2 draws ",sec_card_chosen)
    else:
        return
    if fir_card_chosen == sec_card_chosen:
        war(player_1, player_2)
    elif fir_card_chosen > sec_card_chosen:
        player_1.extend(face_down_cards_1)
        player_1.extend(face_down_cards_2)
        player_1.append(fir_card_chosen)
        player_1.append(sec_card_chosen)
        player_2.remove(face_down_cards_2)
        player_2.remove(face_down_cards_1)
        player_2.remove(fir_card_chosen)
        player_2.remove(sec_card_chosen)
    else:
        player_2.extend(face_down_cards_1)
        player_2.extend(face_down_cards_2)
        player_2.append(fir_card_chosen)
        player_2.append(sec_card_chosen)
        player_1.remove(face_down_cards_2)
        player_1.remove(face_down_cards_1)
        player_1.remove(fir_card_chosen)
        player_1.remove(sec_card_chosen)
        return player_1, player_2

"""
Game Instructions
1) The objective of the game is to win all of the cards.
2) The deck is divided evenly among the players 
3) In unison, each player reveals the top card of their deck—this is a "battle"
4) player with the higher card takes both of the cards played and moves them to their stack.
5) Aces are high, and suits are ignored.
6) If the two cards played are of equal value, then there is a "war".
7) Both players place the one card face down and then another card face-up.
Finishing current step: 
8) The owner of the higher face-up card wins the war and adds all the cards on the table to the bottom of their deck.
9) If the face-up cards are again equal then the battle repeats with another set of face-down/up cards. This repeats until one player's face-up card is higher than their opponent's.
10) Ask the player if they want to play again.  
11) Quit if they say no, and start from the beginning if they say yes. 

"""

        

