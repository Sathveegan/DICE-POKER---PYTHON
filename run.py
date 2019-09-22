import random
import dice

#
# Display Details
# #
def display_details():
    print('File : run.py')
    print('Author : Sathveegan')
    print('This is a Python program that allows a player to play a game of dice poker against the computer.')

#
# Return a random number between 1 and six
# #
def roll_die():
    return random.randint(1, 6)

#
# Return a player / dealer hand array using max dice
# #
def deal_hand(max_dice):
    player_hand = []
    for dice in range(max_dice):
        player_hand.append(roll_die())
    return player_hand

#
# Return a rank number using player / dealer hand 
# #
def rank_hand(hand):
    rank = 0
    die_count = [0, 0, 0, 0, 0, 0, 0]
    
    for index in range(len(hand)):
        die_value = hand[index]
        die_count[die_value] = die_count[die_value] + 1
    
    for index in range(1, len(die_count)):
        if die_count[index] == 5:
            rank = 6
        elif die_count[index] == 4:
            rank = 5
        elif die_count[index] == 3:
            rank = 3
            for i in range(1, len(die_count)):
                if die_count[i] == 2:
                    rank = 4
        elif die_count[index] == 2:
            rank = 1
            for i in range(1, len(die_count)):
                if i != index and die_count[i] == 2:
                    rank = 2

    return rank

#
# Display the rank name using rank number
# #
def display_rank(rank):
    if rank == 6:
        print('Five of a kind')
    elif rank == 5:
        print('Four of a kind')
    elif rank == 4:
        print('Full house')
    elif rank == 3:
        print('Three of a kind')
    elif rank == 2:
        print('Two pairs')
    elif rank == 1:
        print('One pair')
    elif rank == 0:
        print('Nothing special')

#
# Main method of Dice Poker game
# #
def main():

    display_details()

    game_won = 0
    game_lost = 0
    game_draw = 0

    again = True
    
    while again:

        answer = input('\nWould you like to play dice poker [y|n]? ')

        while answer != 'y' and answer != 'n':
            print('Please enter either \'y\' or \'n\'.')
            answer = input('\nWould you like to play dice poker [y|n]? ')

        if answer == 'n':
            again = False
            total_game = game_won + game_lost + game_draw

            if total_game == 0:
                print('\nNo worries... another time perhaps... :)\n')
            else:
                print('\nGame Summary')
                print('============')
                print('You played ' + str(total_game) + ' games')
                print('\t|--> Games won: ' + str(game_won))
                print('\t|--> Games lost: ' + str(game_lost))
                print('\t|--> Games drawn: ' + str(game_draw))
                print('\nThanks for playing!\n')

        else:
            player_hand = deal_hand(5)
            dealer_hand = deal_hand(5)

            print('\nPlayer\'s hand: ')
            dice.display_hand(player_hand, 5)
            print('\nDealer\'s hand: ')
            dice.display_hand(dealer_hand, 5)

            player_rank = rank_hand(player_hand)
            dealer_rank = rank_hand(dealer_hand)

            print('\n-- Player has', end = ' ')
            display_rank(player_rank)
            print('-- Dealer has', end = ' ')
            display_rank(dealer_rank)

            if player_rank > dealer_rank:
                print('\n** Player wins! **')
                game_won = game_won + 1
            elif player_rank == dealer_rank:
                print('\n** Draw! **')
                game_draw = game_draw + 1
            else:
                print('\n** Dealer wins! **')
                game_lost = game_lost + 1
        
#
# Call the main method
# #
main()
