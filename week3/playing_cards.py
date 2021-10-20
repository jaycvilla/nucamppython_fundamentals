import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while True:
    card_chosen = [0]
    card = input("Pick a card, or Q then enter to quit ")
    if card == "Q":
        break
    if not diamonds:
        print("There are no more cards to pick.")
        break
    else:  
        card_chosen = random.choice(diamonds) 
        hand.append(card_chosen)
        print("Your Hand: ", hand) 
        diamonds.remove(card_chosen)
        print("Remaining Cards: ", diamonds)
    
