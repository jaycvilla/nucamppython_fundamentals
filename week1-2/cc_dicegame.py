import random

high_score = 0
total_roll = 0

def dice_game():
    while True:
        print("1) Roll Dice")
        print("2) Leave Game")
        choice = input("Enter your choice: ")
        global total_roll
        if choice == "1":
            roll_1 = random.randint(1,6)
            print("You roll a... ",roll_1, "\n")
            roll_2 = random.randint(1,6)
            print("You roll a... ",roll_2, "\n")
            total_roll = roll_1 + roll_2
            print("You have rolled a total of: ", total_roll, "\n")
            if high_score < total_roll: 
                print("New high score!\n\nCurrent high Score: ", total_roll)
                dice_game()
            else: 
                dice_game()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Unknown Character")
            break
        

dice_game()




