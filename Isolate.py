from colorama import Fore, Back, Style
import os
import random

def Shoot_Guess(Grid, col_list, row_list,turn):
  
  while True:
        
        if turn == 0:

            shot = (f" {chr(random.randint(65, 65 + row_list - 1) )}{random.randint(1,col_list)}").strip().replace(",", "")

        else:

            shot = input(f"Where do you want to shoot (A-{chr(65 + row_list - 1)},1-{col_list})? ").strip().replace(",", "")
            
        # .lower is case insinstive 

        if shot.lower() == "quit":

            print("The game has been forced quit. Have a nice day!")
            quit()

        #ensures length of character is atleast 2 | checks if first character is valid and within range | ensures character is digit *valid column number coverts & into int
        
        elif len(shot) >= 2 and shot[0].upper() in [chr(65 + i) for i in range(row_list)] and shot[1:].isdigit() and int(shot[1:]) <= col_list:
            break

        else:

            print(f"Invalid input. Please enter a valid coordinate (A-{chr(65 + row_list - 1)},1-{col_list}).")
            print (shot)

        # generate shot coordinates
        #example: ord('B') - ord('A') gives 66 - 65 = 1
        row = ord(shot[0].upper()) - ord('A')
        #shot[1] = int value | number value
        col = int(shot[1:]) - 1

        X = "x"
        Grid[row][col] = f"{Fore.LIGHTYELLOW_EX}{X}{Fore.BLUE}"
        return (Grid, X)
  

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.WHITE +"Welcome to Battleship!")

    print(Fore.RED +   " ______           _     _   __                __        _                                                         ___#_#___|__")                                          
    print(Fore.RED +   "|_   _ \         / |_  / |_[  |              [  |      (_)                                                    _  |____________|  _")                             
    print(Fore.RED +   "  | |_) |  ,--. `| |-'`| |-'| | .---.  .--.   | |--.   __  _ .--.                                    =====| |.---------------------------. | |====")                            
    print(Fore.WHITE + "  |  __'. `'_\ : | |   | |  | |/ /__\\( (`\]  | .-. | [  |[ '/'`\ \                <--------------------'   .  .  .  .  .  .  .  .   '--------------/")                        
    print(Fore.WHITE + " _| |__) |// | |,| |,  | |, | || \__., `'.'.  | | | |  | | | \__/ |                 __..._____--==/___]_|__|_____________________________[___\==--____,------' .7")                   
    print(Fore.BLUE +  "|_______/ \'-;__/\__/  \__/[___]'.__.'[\__) )[___]|__][___]| ;.___/                 |                                                                     BB-61/")               
    print(Fore.BLUE +  "                                                           [__|                    \_______________________________________________WWS______________________/")

    print(f"""{Fore.RED}Description:
    {Fore.LIGHTBLACK_EX}    The game starts with a grid of your choosing displayed on the screen.
        You will be prompted to input the coordinates where you want to shoot.
        Coordinates should be in the format X,# (e.g., A,1).
        If your shot hits the ship, you win and the game ends.
        If your shot misses, you can try again.
        The game will update the grid after each shot to reflect the shots fired.
    {Fore.RED}    Please enter \"Quit\" at any time to end the game.\n""")

    #///////////////////////////////////////////////////////////////////////////(Inputs For Grid Creation and Intitializing Grids)\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    # print(Fore.WHITE+"Create Your Grid: ")
    col_list = 10
    row_list = 10
    turn = 0
    # Gianna
    # Initialize grids
    computerDisplayGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]
    # computerCoordGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]

    playerDisplayGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]
    # playerCoordGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]

    # Display initial ship placement grid
    BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list)

    #////////////////////////////////////////////////////////////////////////////////////(Inputs For Usership Placement)\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    # Input for player ship 2x1
    playerShips = {}

    playerShip1_name = input("\nName your first ship: ")

    # Input for player ship 1

    while True:

        while True:

            while True:

                ship1 = input(f"\nPlease enter the front coordinate for your ship, {playerShip1_name} (A-{chr(65 + row_list - 1)},1-{col_list}): ").strip().replace(",", "")

                if ship1.lower() == "quit":

                    print("The game has been forced quit. Have a nice day!")
                    quit()

                elif len(ship1) >= 2 and ship1[0].upper() in [chr(65 + i) for i in range(row_list)] and ship1[1:].isdigit() and int(ship1[1:]) <= col_list:

                    break

                else:

                    print(f"Invalid input. Please enter a valid coordinate (A-{chr(65 + row_list - 1)},1-{col_list}).")

            break

        # generates coords of the player ship 2x1
        row1 = ord(ship1[0].upper()) - ord('A')
        col1 = int(ship1[1:]) - 1
        playerDisplayGrid[row1][col1] = f"{Fore.LIGHTRED_EX}O{Fore.BLUE}"
        BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list)
        
        # asks and defines orientation for 2x1 ship
        orientation = input(f"Choose your ship orientation for {playerShip1_name} (v for vertical, h for horizontal): ").strip()

        while True:

            if orientation != "h" and orientation != "v" :

                os.system('cls' if os.name == 'nt' else 'clear')
                BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list)
                orientation = input(f"Choose your ship orientation(v for vertical, h for horizontal): ").strip()

            else:

                break

        while True:

            if orientation == "v":

                if row1 < row_list-1:

                    row2 = row1 + 1
                    col2 = col1 
                    break

                else:

                    row2 = row1 - 1
                    col2 = col1
                    break

            else:

                break

        while True:      

            if orientation == "h":

                if col1 < col_list-1:
                    row2=row1
                    col2=col1 + 1
                    break

                else:

                    row2=row1
                    col2=col1 - 1
                    break

            else:

                break
        
        playerDisplayGrid[row2][col2] = f"{Fore.LIGHTRED_EX}O{Fore.BLUE}"
        BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list)

        while True:
                
                satisfied = input(f"Is this where you want {playerShip1_name}? (Y/N): ").strip()

                if satisfied.lower() == "y":
                    break

                elif satisfied.lower() != "n":

                    print(f"Invalid input. Please enter Y or N: ")

                else:

                    playerDisplayGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]
                    break

        if satisfied.lower() == "y":
            break

    playerShips.update({playerShip1_name: [f"First Coord: ({row1}, {col1})   Second Coord: ({row2}, {col2})"]})

    playerShip2_name = input("Name your second ship: ")

    # Input for player ship 2

    while True:

        while True:

            while True:

                ship2 = input(f"Please enter the front coordinate for your ship, {playerShip2_name} (A-{chr(65 + row_list - 1)},1-{col_list}): ").strip().replace(",", "")

                if ship2.lower() == "quit":

                    print("The game has been forced quit. Have a nice day!")
                    quit()

                elif len(ship2) >= 2 and ship2[0].upper() in [chr(65 + i) for i in range(row_list)] and ship2[1:].isdigit() and int(ship2[1:]) <= col_list:

                    break

                else:

                    print(f"Invalid input. Please enter a valid coordinate (A-{chr(65 + row_list - 1)},1-{col_list}).")
            break

        # generates coords of the player ship 2x1
        row3 = ord(ship2[0].upper()) - ord('A')
        col3 = int(ship2[1:]) - 1
        playerDisplayGrid[row3][col3] = f"{Fore.LIGHTRED_EX}O{Fore.BLUE}"
        BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list)
        
        # asks and defines orientation for 2x1 ship
        orientation = input(f"Choose your ship orientation for {playerShip2_name} (v for vertical, h for horizontal): ").strip()

        while True:

            if orientation != "h" and orientation != "v" :

                os.system('cls' if os.name == 'nt' else 'clear')
                BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list)
                orientation = input(f"Choose your ship orientation(v for vertical, h for horizontal): ").strip()

            else:

                break

        while True:

            if orientation == "v":

                if row3 < row_list-1:
                    row4 = row3 + 1
                    col4 = col3 
                    break

                else:

                    row4 = row3 - 1
                    col4 = col3
                    break

            else:

                break

        while True:      

            if orientation == "h":

                if col3 < col_list-1:
                    row4 = row3
                    col4 = col3 + 1
                    break

                else:

                    row4 = row3
                    col4 = col3 - 1
                    break

            else:

                break
        
        playerDisplayGrid[row4][col4] = f"{Fore.LIGHTRED_EX}O{Fore.BLUE}"
        BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list)

        while True:
                
                satisfied = input(f"Is this where you want {playerShip2_name}? (Y/N): ").strip()

                if satisfied.lower() == "y":

                    break

                elif satisfied.lower() != "n":

                    print(f"Invalid input. Please enter Y or N: ")

                else:

                    playerDisplayGrid[row3][col3] = " "
                    playerDisplayGrid[row4][col4] = " "
                    break

        if satisfied.lower() == "y":

            os.system('cls' if os.name == 'nt' else 'clear')
            break

    playerShips.update({playerShip2_name: [f"First Coord: ({row3}, {col3})   Second Coord: ({row4}, {col4})"]})

#///////////////////////////////////////////////////////////////////////////(Inputs For Computer Ship Placement)\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#   
# Initialize ship positions for computer randomly

    computerShips = {}

    computerShip1_name = input("\nName the computer's first ship: ")

    random_num1 = random.randint(0, row_list - 1)
    random_num2 = random.randint(0, col_list - 1)

    computerShips.update({computerShip1_name: [f"First Coord: ({random_num1}, {random_num2})"]})
    print(computerShips) #----------------------------------------------------------------------------------------------
 
    while True:

        if random_num1 != row1 and random_num2 != row2 and random_num2 != col1 and random_num2 != col2:
            break

        else:

            random_num1 = random.randint(0, row_list - 1)
            random_num2 = random.randint(0, col_list - 1)

    # Alternates turns between the computer and the player
    while True:

        turn=0

        if turn == 0:

                # prints list of ships and coords for testing

                # for x, y in computerShips.items():
                #     print(f"- {x}, {y}")

                print("\nComputer objective: Sink The Player's Ships\n")
                Shoot_Guess(playerDisplayGrid, col_list, row_list,turn)
                BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list)

                if playerDisplayGrid[row1][col1] and playerDisplayGrid[row2][col2] and playerDisplayGrid[row3][col3] and playerDisplayGrid[row4][col4] == "x":

                    print("The computer sunk both your ships! Better luck next time.")
                    win_animation(turn)
                    
                # Check if player hits ship 1 or ship 2
                print("\nMove Log:")

                if playerDisplayGrid[row1][col1] == "x":

                    print(f"The computer hit your ship, {playerShip1_name}!")

                if playerDisplayGrid[row2][col2] == "x":

                    print(f"The computer hit your ship, {playerShip1_name}!")

                if playerDisplayGrid[row3][col3] == "x":

                    print(f"The computer hit your ship, {playerShip2_name}!")

                if playerDisplayGrid[row4][col4] == "x":

                    print(f"The computer hit your ship, {playerShip2_name}!")

                if playerDisplayGrid[row1][col1] and playerDisplayGrid[row2][col2] == "x":

                    print(f"The computer sunk your ship, {playerShip1_name}!")

                if playerDisplayGrid[row3][col3] and playerDisplayGrid[row4][col4] == "x":

                    print(f"The computer sunk your ship, {playerShip2_name}!")

                else:

                    print("\nThe computer missed!")

                t=5

                while t > 0:

                    print(f"{Fore.WHITE}Player moves in {t % 60:02}", end=" seconds.\r")  # display minutes and seconds
                    time.sleep(1)  # wait for 1 second
                    t -= 1

                os.system('cls' if os.name == 'nt' else 'clear')

        turn = 1

        if turn == 1:

            # prints list of ships and coords for testing

            # for x, y in playerShips.items():
            #     print(f"- {x}, {y}")

            BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list)
            Shoot_Guess(computerDisplayGrid, col_list, row_list,turn)

            if computerDisplayGrid[random_num1][random_num2] != "x":

                shipAnimation_hit_miss(0)

            # Check if player hits ship 1 or ship 2

            if computerDisplayGrid[random_num1][random_num2] == "x":

                shipAnimation_hit_miss(1)
                print("You sunk the Computer's ship! You WIN!")
                win_animation(turn)
                t=10

                while t > 0:

                    print(f"{Fore.WHITE}Back to menu in {t % 60:02}", end = " seconds.\r")  # display minutes and seconds
                    time.sleep(1)  # wait for 1 second
                    t -= 1

                main()
                
                os.system('cls' if os.name == 'nt' else 'clear')

        os.system('cls' if os.name == 'nt' else 'clear')  
        
    
#///////////////////////////////////////////////////////////////////////////(Calling The Game() Funtion)\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#        
# Entire functioning program: 206 lines
# (Lines w/out animations)        
main()
