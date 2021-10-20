import random

def guess_random_number(tries, start, stop):
    number = random.randint(start, stop)

    while tries != 0:
        print('Number of tries left: ', tries)
        guess = int(input("Guess a number between 1 and 10: "))
        tries -= 1
        if guess < number:
            print('Guess higher!')
            
        if guess > number:
            print('Guess lower!')
            
        if guess == number:
            break
    if guess == number:
        print('You guessed the correct number', str(number))
    else:
        print('You did not guess the number: ', str(number))

#guess_random_number(5, 0, 10)

def guess_random_num_linear(tries, start, stop):
    number = random.randint(start, stop)
    print('The number for the program to guess is:', number)
    for x in range(0, 10) :
        if tries != 0:
            tries -= 1
            print('The number for the program to guess is... ', x)
            print('Number of tries left: ', tries)
            if x == number:
                print('You guessed the correct number', str(number))
                return x
        else:
            print('You have failed to guess the correct number.')
            break

#guess_random_num_linear(5, 0, 10)

def binary_search(tries, start, stop):
    number = random.randint(start, stop)
    lower_bound = int(start)
    upper_bound = int(stop)
    print("Random number to find:", number)

    while tries != 0:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = pivot
        tries -= 1
        
        if pivot_value == number:
            print('You guessed the correct number', str(pivot))
            return pivot
        elif pivot_value > number:
            upper_bound = pivot - 1
            print('Guessing Lower!')
        else:
           lower_bound = pivot + 1
           print('Guessing Higher!')
    else:
        print('Your program has failed to find the number')

binary_search(5, 0, 10)



