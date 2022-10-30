#imports the inbuilt python random module
import random

def main_screen():
    """
    A function to generate the main screen before the game starts.
    ASCII art dashboard and asks player to start game.
    Asks player for a name + difficulty.
    """
    print("                                   |__  ") 
    print("                                   |\/")
    print("                                   ---")
    print("                                   / | [")
    print("                           !      | |||")
    print("                           _/|     _/|-++'")
    print("                       +  +--|    |--|--|_ |-")
    print("                   { /|__|  |/\__|  |--- |||__/")
    print("                   +---------------___[}-_===_.'____               /\ ")
    print("               ____`-' ||___-{]_| _[}-  |     |_[___\==--          \/   _")
    print("__..._____--==/___]_|__|_____________________________[___\==--___,-----' .7")
    print("|                                                                        /")
    print("\_______________________________________________________________________| ")

    print("         _ __        _   _   _           _     _   ")    
    print("        |  _ \      | | | | | |         | |   (_) ")     
    print("        | |_)/  __ _| |_| |_| | ___  ___| |__  _ _ __   ___ ")
    print("        | '_ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \ / __| ")
    print("        | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |\__ \ ")
    print("        |_.__/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ |___/ ")
    print("                                                | |   ") 
    print("                                                |_| ")
    name = input("Please enter your name:\n")
    print(f"Welcome Admiral {name}.")
    difficulty = input("Choose your theatre of operations:\n The Mediterranean Sea (Easy),\n The Atlantic Ocean (Normal),\n The Pacific Ocean (Hard).\n")
    print(f"You have selected: {difficulty}")
    return difficulty.lower()

def check_difficulty(difficulty):
    valid_difficulties = {'easy', 'medium', 'hard'}
    try:
        if str(difficulty) not in valid_difficulties:
            raise ValueError(
                "Type in the difficulty level."
                )
    except ValueError as e:
        print(f"{e} Please try again.")
        return False

    return True
        

def run_game():
    """
    Main function. Will incorporate board and ship generation.
    """

class GameBoard():
    """
    Will generate the game board and ships.
    """
    def __init__(self, board):
        self.board = board
    
    def co_ordinates():
        co_ordinates = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8,}
        return co_ordinates
    
    def generate_board(self):
        print(" A B C D E F G H I ")
        print(" x-x-x-x-x-x-x-x-x ")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1

class Warship:
    def __init__(self, board):
        self.board = board
    
    def generate_fleet(self):
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 8), random.randint(0, 8)
            while self.board[self.x_row][self.y_row] == "X":
               self.x_row, self.y_column = random.randint(0, 8), random.randint(0, 8)
            while self.board[self.x_row][self.y_row] == "X"
        return self.board
    
    def user_fire_mission(self):
        try:
            x_row = input("Enter X Co-Ordinate for Fire Mission: ")
            while x_row not in "123456789":
                print("Invalid co-ordinate. Enter another.")
                x_row = input("Enter X Co-Ordinate for Fire Mission: ")
            
            y_column = input("Enter Y Co-Ordinate for Fire Mission: ").upper()
            while y_column not in "ABCDEFGHI":
                print("Invalid co-ordinate. Enter another.")
                y_column = input("Enter Y Co-Ordinate for Fire Mission: ").upper()
            return int(x_row) -1, GameBoard.co_ordinates()[y_column]
        except ValueError and KeyError:
            Print("Not a valid input.")
            return self.user_fire_mission()

        




def generate_ships():
    """
    Will generate a series of ships.
    Ship sizes preset but locations generated randomly.
    """

def ship_shooting():
    """
    Takes the user input and checks for validation.
    Assigns the shot to a co-ordinate and checks for hit/miss/sink.
    Generates computer shot.
    Feeds back to user.
    """

def game_over():
    """
    Runs when all ships sunk.
    Prompts user to restart or exit.
    """

difficulty = main_screen()
check_difficulty(difficulty)