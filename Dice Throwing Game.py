"""
Ish Gill
A user vs computer dice throwing game!
"""
import random

def main():
    username = "Ish Gill"
    player_name = "Ish"
    option_new_game = 1
    option_see_stats = 2
    option_quit = 0

    number_of_games = 0
    won_by_user = 0
    won_by_computer = 0

    display_introduction('   ', username, player_name)
    selection = option_new_game

    while selection !=  option_quit:
        selection = get_main_menu_selection(" " * 5)

        if selection == option_new_game:
            number_of_games += 1
            winner_name = play_a_game(player_name)

            if winner_name == player_name:
                won_by_user += 1
            elif winner_name == "Computer":
                won_by_computer += 1

        elif selection == option_see_stats:
            display_statistics(player_name, number_of_games, won_by_user, won_by_computer)

    display_statistics(player_name, number_of_games, won_by_user, won_by_computer)
    print()
    print("Thank you for playing Ventuno " + player_name)
    print()


def display_line_of_symbols(indent, symbol, how_many):
    symbol_quantity = symbol * how_many
    indents = indent + "" + symbol_quantity 
    return print(indents)

def display_introduction(indent, username, name):
        print()
        symbol_line= display_line_of_symbols(indent, "=", 27)
        display_string = indent + "Ventuno written by " + username
        print(display_string)
        welcome_string = indent + "Welcome " + name
        print(welcome_string)
        symbol_line= display_line_of_symbols(indent, "=", 27)
        print()
        return 


def get_play_menu_selection(indent):
        print()
        selection1 = indent + "1. ROLL" + " \n" + indent + "2. STAY"
        print(selection1)
        user_prompt = str(input(indent + "   Enter selection: "))
        user_selection = str(user_prompt)
        user_return = int(user_selection)
        return user_return

def get_main_menu_selection(indent):
        print()
        menu_selection = (indent + "1. PLAY A NEW GAME" + " \n" + indent + "2. SEE STATS"
        "\n" + indent + "0. QUIT")
        print(menu_selection)
        user_prompt = str(input(indent + "   Enter selection: "))
        user_selection = str(user_prompt)
        user_return = int(user_selection)
        return user_return


def display_current_player(current_player):
    current_player = current_player + "'s turn:"
    return print(current_player)

def get_next_player(current_player, player_name):
    if current_player == "Computer":
        return player_name
    else:
        return "Computer"
    

def get_random_starting_player_name(player_name):
    name = random.randrange(1, 3)
    if name == 1:
        return player_name
    else:
        return "Computer"
    

def add_dice_roll(current_score, current_player):
    dice = random.randrange(1, 7)
    current_player = current_player + "" + "'s dice roll: " + "" + str(dice)
    print(current_player)
    current_score = int(dice) + int(current_score)
    return current_score

def get_starting_score():
    starting_score = random.randrange(12, 17)
    return starting_score


def display_current_scores(indent, score_player, score_computer, player_stays, computer_stays, player_name):
    print()
    rows_of_symbols = display_line_of_symbols(indent, "-", 37)
    rows_of_symbols = display_line_of_symbols(indent, "-", 37)
    if player_stays and player_stays:
        current_player = indent + player_name + "'s score: " + str(score_player) + " - " + player_name + " stays"
    else: current_player = indent + player_name + "'s score: " + str(score_player)
    print(current_player)
    if computer_stays and computer_stays:
        computer = indent + "" + "Computer's score: " + str(score_computer) + " - " + "Computer" + " stays"
    else: computer = indent + "" + "Computer's score: " + str(score_computer)
    print(computer)
    rows_of_symbols = display_line_of_symbols(indent, "-", 37)
    rows_of_symbols = display_line_of_symbols(indent, "-", 37)    
    return 

def game_is_over(score_player, score_computer, player_stays, computer_stays):
    if player_stays and computer_stays:
        return True
    elif score_player > 21 or score_computer > 21:
        return True
    return False

def get_winner_name(score_player, score_computer, player_name):
    if score_player == score_computer:
        return "draw"
    elif score_player > 21:
        return "Computer"
    elif score_computer > 21:
        return player_name
    elif  score_player > score_computer:
        return player_name
    else:
        return "Computer"

def display_game_result(indent, score_player, score_computer, game_winner, player_name):
    print()
    rows_of_symbols = display_line_of_symbols(indent, "+", 25)
    rows_of_symbols = display_line_of_symbols(indent, "+", 25)
    player_score = indent + player_name + "'s score: " + str(score_player)
    print(player_score)
    computer_score = indent + "Computer's score: " + str(score_computer)
    print(computer_score)
    if game_winner == "Computer":
        print(indent + "Computer has won.")
    elif game_winner == player_name:
        print(indent + player_name + " has won.  Well done!")
    else:
        if game_winner != player_name or "Computer":
            print(indent + "Result is a " + game_winner + ".")
    rows_of_symbols = display_line_of_symbols(indent, "+", 25)
    rows_of_symbols = display_line_of_symbols(indent, "+", 25)
    return 

def display_statistics(player_name, total_number_of_games, games_won_by_user, games_won_by_computer):
    print()
    rows_of_symbols = "*" * 32
    print(rows_of_symbols)
    print(rows_of_symbols)
    draws = total_number_of_games - games_won_by_user - games_won_by_computer
    player_difference = games_won_by_user - games_won_by_computer
    computer_difference = games_won_by_computer - games_won_by_user
    print("Number of games played: " + str(total_number_of_games))
    print("Games won by " + player_name + ": " + str(games_won_by_user))
    print("Games won by Computer: " + str(games_won_by_computer))
    print("Games resulting in a draw: " + str(draws))
    print()
    if games_won_by_user > games_won_by_computer:
        print("*** " + player_name + " is winning by " + str(player_difference) + " ***")
        print(rows_of_symbols)
        print(rows_of_symbols)
    elif games_won_by_computer > games_won_by_user:
        print("*** Computer is winning by " + str(computer_difference) + " ***")
        print(rows_of_symbols)
        print(rows_of_symbols)
    elif draws > games_won_by_computer and draws > games_won_by_user:
        print("*** Final result is a draw ***")
        print(rows_of_symbols)
        print(rows_of_symbols)


def get_computer_selection(score_player, score_computer, player_stays):
    roll = 1
    stay = 2
    ventuno = 21
    if score_player >= score_computer and score_player <= 19: 
        return roll
    elif score_player >= 18 and score_computer >= 19 and player_stays:
         return stay
    elif score_computer > score_player and score_computer >= 19:
         return stay
    elif score_computer == score_player and score_player >= ventuno - 1:
         return stay
    return roll

def play_a_game(player_name):
    ventuno = 21

    player_stays = False
    computer_stays = False

    roll = 1
    stay = 2

    score_player = get_starting_score()
    score_computer = get_starting_score()

    current_player = get_random_starting_player_name(player_name)
    display_current_scores(" " * 5, score_player, score_computer, player_stays, computer_stays, player_name)

    while not game_is_over(score_player, score_computer, player_stays, computer_stays):
        if current_player == "Computer":
            if not computer_stays:
                display_current_player(" " + current_player)
                selection = get_computer_selection(score_player, score_computer, player_stays)

                if selection == roll:
                    score_computer = add_dice_roll(score_computer, "  Computer")
                    if score_computer == ventuno:
                        computer_stays = True
                else:
                    computer_stays = True
        elif not player_stays:
            display_current_player(" " + current_player)
            selection = get_play_menu_selection(' ' * 3)
            print()
            if selection == roll:
                score_player = add_dice_roll(score_player, " " + player_name)
                if score_player == ventuno or (computer_stays and score_player > score_computer):
                    player_stays = True
            elif selection == stay:
                player_stays = True

        display_current_scores(" " * 5, score_player, score_computer, player_stays, computer_stays, player_name)
        current_player = get_next_player(current_player, player_name)


    game_winner = get_winner_name(score_player, score_computer, player_name)
    display_game_result("  ", score_player, score_computer, game_winner, player_name)
    return game_winner

main()
