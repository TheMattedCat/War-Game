import random

def convert_card_type(card):
    if card[0] in [11, 12, 13, 14]:
        card[0] = 11
        return "the sons"
    elif card[0] == 12:
        return "the mums"
    elif card[0] == 13:
        return "the dads"
    elif card[0] == 14:
        return "the butlers"
    elif card[0] == 15:
        return "1"
    else:
        return str(card[0])

def convert_card_suite(card):
    if card[1] == 1:
        return 'Belts'
    elif card[1] == 2:
        return 'Swords'
    elif card[1] == 3:
        return 'Bazooka' 
    elif card[1] == 4:
        return 'sandals'

def result(p1_card, pc_card):
    if p1_card > pc_card:
        return "you finally won"
    elif p1_card < pc_card:
        return "computer win, YOU A FAILURE YOU LOST,BRUH"
    else:
        return "Cant you win a game, Tie, DUDE GET A WIN "

deck = [[number, suite] for number in range(2, 15) for suite in range(1, 5)]
random.shuffle(deck)

print("Welcome to the war Game!")

while True:
    input('Press enter to draw a weapon: ')

    try:
        p1_card = deck.pop()
    except IndexError:
        print("You ran out of people. PLAY AGAIN!")
        break

    pc_card = deck.pop()

    p1_name = convert_card_type(p1_card) + ' ' + convert_card_suite(p1_card)
    pc_name = convert_card_type(pc_card) + ' ' + convert_card_suite(pc_card)

    print('\nPlayer drew:', p1_name)
    print('Computer drew:', pc_name)

    round_result = result(p1_card[0], pc_card[0])
    print("\n" + round_result)

    print(f'\nRemaining cards in deck: {len(deck)}')

    play_again = input('\nDo you want to play again? (yes/no): ')
    if play_again.lower() != 'yes':
        print("\nThanks for playing! now DIE!")
        break
