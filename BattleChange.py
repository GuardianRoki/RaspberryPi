import random
import os
from colorama import init, Fore, Style
import time


####################################################(Animations)############################################################### 
#V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V 


####################################################(Animations - Cameron)############################################################### 
# shipAnimation_miss(), shipAnimation_hit(), computer_win(), player_win() are all just animations put into a function

def shipAnimation_hit_miss(hit):
    if hit == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(""""                                   
                                            ---
                                            / | [
                                    !      | |||
                                    _/|     _/|-++'
                                +  +--|    |--|--|_ |-
                            { /|__|  |/\__|  |--- |||__/
                            +---------------___[}-_===_.'____           ___      
                        ____`-' ||___-{]_| _[}-  |     |_[___\==--     /___===      _
        __..._____--==/___]_|__|_____________________________[___\==--|___|,------' .7
        |                                                                     BB-61/
        \_________________________________________________________________________|""")
        time.sleep(.2)
        os.system('cls' if os.name == 'nt' else 'clear')

        print(""""                                   
                                            ---
                                            / | [
                                    !      | |||
                                    _/|     _/|-++'
                                +  +--|    |--|--|_ |-
                            { /|__|  |/\__|  |--- |||__/                  __
                            +---------------___[}-_===_.'____           __/ /     
                        ____`-' ||___-{]_| _[}-  |     |_[___\==--     /___/     _
        __..._____--==/___]_|__|_____________________________[___\==--|___|,------' .7
        |                                                                     BB-61/
        \_________________________________________________________________________|""")
        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')

        print(""""                                   
                                            ---                            
                                            / | [                         /\ 
                                    !      | |||                          ||
                                    _/|     _/|-++'                       ||
                                +  +--|    |--|--|_ |-                    ** 
                            { /|__|  |/\__|  |--- |||__/                  **
                            +---------------___[}-_===_.'____           __| |     
                        ____`-' ||___-{]_| _[}-  |     |_[___\==--     /___/     _
        __..._____--==/___]_|__|_____________________________[___\==--|___|,------' .7
        |                                                                     BB-61/
        \_________________________________________________________________________|""")
        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(""""                                                    
                                                                        **
                                                                    ********
                                            ---                      ************
                                            / | [                      ******* 
                                    !      | |||                          **
                                    _/|     _/|-++'                        
                                +  +--|    |--|--|_ |-                      
                            { /|__|  |/\__|  |--- |||__/                  
                            +---------------___[}-_===_.'____           __| |     
                        ____`-' ||___-{]_| _[}-  |     |_[___\==--     /___/     _
        __..._____--==/___]_|__|_____________________________[___\==--|___|,------' .7
        """)
    
        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("           _      ")   
        print(" _ __ ___ (_)___ ___ ")
        print("| '_ ` _ \| / __/ __|")
        print("| | | | | | \__ \__ \ ")
        print("|_| |_| |_|_|___/___/")    
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

        

    ####################################################(Animations)############################################################### 
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(""""                                   
                                            ---
                                            / | [
                                    !      | |||
                                    _/|     _/|-++'
                                +  +--|    |--|--|_ |-
                            { /|__|  |/\__|  |--- |||__/
                            +---------------___[}-_===_.'____           ___      
                        ____`-' ||___-{]_| _[}-  |     |_[___\==--     /___===      _
        __..._____--==/___]_|__|_____________________________[___\==--|___|,------' .7
        |                                                                     BB-61/
        \_________________________________________________________________________|""")
        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')

        print(""""                                   
                                            ---
                                            / | [
                                    !      | |||
                                    _/|     _/|-++'
                                +  +--|    |--|--|_ |-
                            { /|__|  |/\__|  |--- |||__/                  __
                            +---------------___[}-_===_.'____           __/ /     
                        ____`-' ||___-{]_| _[}-  |     |_[___\==--     /___/     _
        __..._____--==/___]_|__|_____________________________[___\==--|___|,------' .7
        |                                                                     BB-61/
        \_________________________________________________________________________|""")
        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')

        print(""""                                   
                                            ---                            
                                            / | [                         /\ 
                                    !      | |||                         ||
                                    _/|     _/|-++'                        ||
                                +  +--|    |--|--|_ |-                     ** 
                            { /|__|  |/\__|  |--- |||__/                  **
                            +---------------___[}-_===_.'____           __| |     
                        ____`-' ||___-{]_| _[}-  |     |_[___\==--     /___/     _
        __..._____--==/___]_|__|_____________________________[___\==--|___|,------' .7
        |                                                                     BB-61/
        \_________________________________________________________________________|""")
        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(""""                                                                  /\ 
                                                                        || 
                                            ---                           || 
                                            / | [                         ** 
                                    !      | |||                         **
                                    _/|     _/|-++'                        
                                +  +--|    |--|--|_ |-                      
                            { /|__|  |/\__|  |--- |||__/                  
                            +---------------___[}-_===_.'____           __| |     
                        ____`-' ||___-{]_| _[}-  |     |_[___\==--     /___/     _
        __..._____--==/___]_|__|_____________________________[___\==--|___|,------' .7
        """)
        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(""""
                            _____
                        ____/     \_____                                   /\ 
                    __/    \________   \                                  ||
                    /                \   \                                 ||
                    |________________|____\                                **
                                            ---                           ** 
                                            / | [                          
                                    !      | |||                         
                                    _/|     _/|-++'                        
                                +  +--|    |--|--|_ |-                     
                            { /|__|  |/\__|  |--- |||__/                     
        """)
        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(""""
                                                                        /\ 
                                                                        ||      
                                                                        ||
                            _____                                         **
                        ____/     \_____                                   ** 
                    __/    \________   \                                  
                    /                \   \                                 
                    |________________|____\                                
                                            ---                            
                                            / | [                          
                                    !      | |||                                                                           
        """)
        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(""""
            
                                                                        /\      
                                                                        ||      
                                                                        ||      
                                                                        **
                                                                        **

                            _____                                         
                        ____/     \_____                                    
                    __/    \________   \                                                                                                 
        """)

        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(""""
            
            
            
                                                                        /\      
                                                                        ||      
                                                                        ||      
                                                                        **
                                                                        **
                                                                                                                                    
        """)

        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(""""
            
            
            
            
            
            
                                                                        /\      
                                                                        ||      
                                                                        ||      
                                                                        **                                                                                              
        """)

        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(""""
            
            
            
            
            
            


                                                                                                                
        """)



        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(""""
            
            
            
            
            
            
                                                                        **
                                                                        **                                                                                                       
        """)


        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(""""
            
            

                                                                        **
                                                                        **   
                                                                        ||
                                                                        ||
                                                                        \/
                                                                        
                                                                                                                                                                            
        """)

        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(""""
                                                                        **
                                                                        **   
                                                                        ||
                                                                        ||
                                                                        \/
                                                                        
                                                                    
                                                                                                
                                                        ---
                                                        / | [
                                                !      | |||
                                                _/|     _/|-++'
                                            +  +--|    |--|--|_ |-                                                                                                                                                                       
        """)

        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(""""
        
                                                                        
                                                                        **
                                                        ---                **
                                                        / | [              ||
                                                !      | |||               ||
                                                _/|     _/|-++'            \/
                                            +  +--|    |--|--|_ |-         
                                        { /|__|  |/\__|  |--- |||__/
                                        +---------------___[}-_===_.'____           ___      
                                    ____`-' ||___-{]_| _[}-  |     |_[___\==--     /___===      _                                                                                                                                                               
        """)


        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(""""
                    
                                                        ---
                                                        / | [
                                                !      | |||                **
                                                _/|     _/|-++'             **
                                            +  +--|    |--|--|_ |-          ||
                                        { /|__|  |/\__|  |--- |||__/        ||
                                        +---------------___[}-_===_.'____   \/      ___      
                                    ____`-' ||___-{]_| _[}-  |     |_[___\==--     /___===      _
                    __..._____--==/___]_|__|_____________________________[___\==--|___|,------' .7
                    |                                                                     BB-61/
                    \_________________________________________________________________________|                                                                                                                                                             
        """)

        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(""""
                                        
                                        
                                    
                                    
                    
                                    

                                                .-=||  | |=-.   
                                                `-=#$%&%$#=-'   
                                                    | ;  :|     
                                            _____.,-#%&$@%#&#~,._____                                                                                                                                                       
        """)



        time.sleep(.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(""""
            
            
                                            _.-^^---....,,--       
                                        _--                  --_  
                                        \._                   _./  
                                            ```--. . , ; .--'''       
                                                | |   |             
                                            .-=||  | |=-.   
                                            `-=#$%&%$#=-'   
                                                | ;  :|     
                                        _____.,-#%&$@%#&#~,._____                                                                                                                                           
        """)



        time.sleep(.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(""""
                                            _.-^^---....,,--       
                                        _--                  --_  
                                        <                        >)
                                        |                         | 
                                        \._                   _./  
                                            ```--. . , ; .--'''       
                                                | |   |             
                                            .-=||  | |=-.   
                                            `-=#$%&%$#=-'   
                                                | ;  :|     
                                        _____.,-#%&$@%#&#~,._____                                                                                                                           
        """)


        time.sleep(.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(" _     _ _   ")   
        print("| |__ (_) |_ ")
        print("| '_ \| | __|")
        print("| | | | | |_  ")
        print("|_| |_|_|\__|")      

        time.sleep(.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")   
        print("")
        print("")
        print("")
        print("")      
        time.sleep(.4)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(" _     _ _   ")   
        print("| |__ (_) |_ ")
        print("| '_ \| | __|")
        print("| | | | | |_  ")
        print("|_| |_|_|\__|")      
        time.sleep(.4)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")   
        print("")
        print("")
        print("")
        print("")      
        time.sleep(.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(" _     _ _   ")   
        print("| |__ (_) |_ ")
        print("| '_ \| | __|")
        print("| | | | | |_  ")
        print("|_| |_|_|\__|")      
        time.sleep(.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        

####################################################(Animations)############################################################### 
def win_animation(turn):

    if turn == 0:
        print(f"   ___                            _              __    __ _           ")
        print(f"  / __\___  _ __ ___  _ __  _   _| |_ ___ _ __  / / /\ \ (_)_ __  ___ ")
        print(f" / /  / _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__| \ \/  \/ / | '_ \/ __|")
        print(f"/ /__| (_) | | | | | | |_) | |_| | ||  __/ |     \  /\  /| | | | \__ \ ") 
        print(f"\____/\___/|_| |_| |_| .__/ \__,_|\__\___|_|      \/  \/ |_|_| |_|___/")
        print(f"                     |_|                                              ")

        print(Fore.YELLOW+"                            .-=========-.")
        print(Fore.YELLOW+"                            \'-=======-'/")
        print(Fore.YELLOW+"                            _|   .=.   |_")
        print(Fore.YELLOW+"                           ((|  {{1}}  |))")
        print(Fore.YELLOW+"                            \|   /|\   |/")
        print(Fore.YELLOW+"                             \__ '`' __/")
        print(Fore.YELLOW+"                               _`) (`_" )
        print(Fore.YELLOW+"                             _/_______\_")
        print(Fore.YELLOW+"                            /___________\ \n")

    else:
        print("   ___ _                          __    __ _           ")
        print("  / _ \ | __ _ _   _  ___ _ __   / / /\ \ (_)_ __  ___ ")
        print(" / /_)/ |/ _` | | | |/ _ \ '__|  \ \/  \/ / | '_ \/ __|")
        print("/ ___/| | (_| | |_| |  __/ |      \  /\  /| | | | \__ \ ")
        print("\/    |_|\__,_|\__, |\___|_|       \/  \/ |_|_| |_|___/")
        print("               |___/                                  ")
        
        
        print(Fore.YELLOW+"                      .-=========-.")
        print(Fore.YELLOW+"                      \'-=======-'/")
        print(Fore.YELLOW+"                       |   .=.   |_")
        print(Fore.YELLOW+"                     ((|  {{1}}  |))")
        print(Fore.YELLOW+"                      \|   /|\   |/")
        print(Fore.YELLOW+"                       \__ '`' __/")
        print(Fore.YELLOW+"                         _`) (`_" )
        print(Fore.YELLOW+"                       _/_______\_")
        print(Fore.YELLOW+"                      /___________\ \n")



####################################################(End Of Animations)############################################################### 


 
####################################################(Actual Code | Functions)###############################################################  
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV 
 
 

#////////////////////////////////////////////////(Grid Creation Funtions)\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
# Gianna
#int_input() function accounts for edge cases and used to force quit game
def int_input(prompt, selection):
    x = input(prompt)
    while not x.isnumeric() or not int(x) in selection:
        # repeats prompt until satisfactory input
        if x.lower() == "quit":
            # force quits if the player inputs "quit"
            print("The game has been forced quit. Have a nice day!")
            quit()
        else:
            x = input(prompt)
    return int(x)

# Cameron
# battleGrid() function to create and display the battle grid
def BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list):

    # Print nums for columns header
    print("", Fore.BLUE + "|", " ", end="")

    for col in range(col_list):
        if col + 1 == 1:
            print(f"{col + 1}", end="  |")
        else:
            #adds space for formating
            if col < 9:
                print(f"  {col + 1}", end="  |")
            # does not inlcude space to format double digits better
            else:
                print(f" {col + 1}", end="  |")

    print("")
    # Print grid rows
    # Chr() function returns a string representing a character whose Unicode code point is the integer specified.
    # Chr(65) = Capital(A)

    for i in range(row_list):

        print(Fore.BLUE + f"{chr(65 + i)}|", end=" ")  # Print row letters (A, B, C, ...)

        if turn == 1:

            for j in range(col_list):

                print(computerDisplayGrid[i][j], end="   | ")  # Print grid content
            print()

        else:

            for j in range(col_list):

                print(playerDisplayGrid[i][j], end="   | ")  # Print grid content
            print()
            
        

#////////////////////////////////////////////////////////////////(Player Shoot and Computer Shoot Funtion)\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    
def Shoot_Guess(computerDisplayGrid, col_list, row_list,turn):
  
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
        computerDisplayGrid[row][col] = f"{Fore.LIGHTYELLOW_EX}{X}{Fore.BLUE}"
        return (computerDisplayGrid, X)
  
#//////////////////////////////////////////////////////////////////(User Turn and Computer Turn Function)\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
# Gianna
# Function for computer to place ships

############################################################################(Game Logic *Funtion That Runs The Game*)######################################################################################
#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv#



#/////////////////////////////////////////////////////////////////////(^^^^^Title Screen Prompt *Rules and Title of Game^^^^^)\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
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
    print(Fore.WHITE+"Create Your Grid:")
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


                print("\nComputer objective:\nSink The Player's Ships")
                Shoot_Guess(playerDisplayGrid, col_list, row_list,turn)
                BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list)

                if playerDisplayGrid[row1][col1] == playerDisplayGrid[row2][col2] == playerDisplayGrid[row3][col3] == playerDisplayGrid[row4][col4] == "x":

                    print("The computer sunk both your ships! Better luck next time.")
                    win_animation(turn)
                    
            
                # Check if player hits ship 1 or ship 2
                print("Move Log:")

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

                    print("The computer missed!")

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

                    print(f"{Fore.WHITE}Back to menu in {t % 60:02}", end=" seconds.\r")  # display minutes and seconds
                    time.sleep(1)  # wait for 1 second
                    t -= 1

                main()
                
                os.system('cls' if os.name == 'nt' else 'clear')

        os.system('cls' if os.name == 'nt' else 'clear')  
        
        
        
#///////////////////////////////////////////////////////////////////////////(Calling The Game() Funtion)\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#        
# Entire functioning program: 206 lines
# (Lines w/out animations)        
main()