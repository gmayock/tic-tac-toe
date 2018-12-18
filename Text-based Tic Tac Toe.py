import itertools as itt

# Allows the user to select different game board size
game_size = int(input("What size game board do you want? "))

# Set up the game board and how it reacts to input
def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != " ":
            print("This position is already taken! Choose another.")
            return game_map, False
        print("    "+"    ".join([str(i) for i in range(len(game_map))]))

        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map, start = 0):
            print(count, row)
        return game_map, True
    
    except IndexError as e:
        print("Error: please validate input row/column was received as integer --", e)
        return game_map, False
    except Exception as e:
        print("Generic error message --", e)
        return game_map, False

# Defines win conditions
def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != ' ':
            return True
        else:
            return False

    # Horizontal
    for row in game:
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally!")
            return True

    # Diagonal top left to bottom right
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally from top left to bottom right!")
        return True

    # Diagonal bottom left to top right
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally from bottom left to top right!")
        return True

    # Vertical
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} is the winner vertically!")
            return True

    return False


def available_spaces(current_game):
    for i in len(current_game):
        sum(i.count(' '))

# Play the game
play = True
players = ['X', 'O']
while play:

    game = [[' ' for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itt.cycle(players)
    while not game_won:
        current_player = next(player_choice)
        print(f"Current player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("What column to you want to play?: "))
            row_choice = int(input("What row to you want to play?: "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        #Handle wins
        if win(game):
            game_won = True
            again = input("GAME OVER. Again? (Y/N): ")
            if again.upper() == "Y":
                print("ggwp. restarting")
                game_size = int(input("What size game board do you want? "))
            elif again.upper() == "N":
                print("ggwp pce out")
                play = False
            else: 
                print("Not a valid input. Terminating.")
                play = False
        
        # Handle ties
        if game_won == False:
            if (sum(i.count(' ') for i in game)) == 0:
                print("Tie game!")
                game_won = True
                again = input("GAME OVER TIE. Again? (Y/N): ")
                if again.upper() == "Y":
                    print("ggwp. restarting")
                    game_size = int(input("What size game board do you want? "))
                elif again.upper() == "N":
                    print("ggwp pce out")
                    play = False
                else: 
                    print("Not a valid input. Terminating.")
                    play = False