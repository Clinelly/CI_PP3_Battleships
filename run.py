# imports the inbuilt python random module
import random
import datetime
# imports google spreadhseet and google credentials APIs
import gspread
from google.oauth2.service_account import Credentials

# Global variables assigned to allow accress through Google APIS to spreadsheet.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('user_data_sheet')

def login():
    """
    Asks user if they're a new or existing user.
    Asks new users to create login details.
    Checks if existing users have correct information.
    """
    while True:
        print("===================================")
        print("Welcome to the Naval Defence System")
        print("===================================")
        new_old = input("Are you a new user? Y/N \n")

        if check_login(new_old):
            break
    return new_old

def check_login(un_pw):
    try:
        str(un_pw)
        if un_pw not in ['Y', 'y', 'N', 'n']:
            raise ValueError(
                "Invalid Input."
            )
    except ValueError as e:
        print(f"{e} Please type in Y or N.")
        return False

    return True
"""
def new_user():
    un_login = SHEET.worksheet('username')
    pw_login = SHEET.worksheet('password')
    date_login = SHEET.worksheet('datetime')
    if str(new_old) == "Y":
        new_un = input("Enter a username:\n")
        un_lst = str.split(new_un)
        un_login.append_row(un_lst)
        print(f"Welcome Admiral {new_un}")
        new_pw = input("Enter a password:\n")
        pw_lst = str.split(new_pw)
        pw_login.append_row(pw_lst)
        print("Password stored.")

# def old_user():
        elif str(new_old) == "N":
        old_un = input("Enter your username:\n")
        check_un = un_login.find(old_un)
        print(f"{check_un} found.")
        old_pw = input("Enter your password:\n")
        check_pw = pw_login.find(old_pw)
        print(f"{check_pw} verified.")
        print(f"Welcome back Admiral {old_un}")
"""
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
        print("  A B C D E F G H I ")
        print("  x-x-x-x-x-x-x-x-x ")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1

class Warship:
    def __init__(self, board):
        self.board = board
    
    def generate_fleet(self):
        """
        Will generate a series of ships.
        Ship sizes preset but locations generated randomly.
        """
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 8), random.randint(0, 8)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 8), random.randint(0, 8)
            self.board[self.x_row][self.y_column] = "X"
        return self.board
    
    def user_fire_mission(self):
        """
        Takes the user input and checks for validation.
        Assigns the shot to a co-ordinate and checks for hit/miss/sink.
        Feeds back to user.
        """
        try:
            y_column = input("Enter Co-Ordinate (A-I) for Fire Mission: ").upper()
            while y_column not in "ABCDEFGHI":
                print("Invalid co-ordinate. Enter another.")
                y_column = input("Enter Co-Ordinate (A-I) for Fire Mission: ").upper()            
            x_row = input("Enter Co-Ordinate (1-9) for Fire Mission: ")
            while x_row not in "123456789":
                print("Invalid co-ordinate. Enter another.")
                x_row = input("Enter X Co-Ordinate (1-9) for Fire Mission: ")
            return int(x_row) -1, GameBoard.co_ordinates()[y_column]
        except ValueError and KeyError:
            print("Not a valid input. Enter a letter or a number.")
            return self.user_fire_mission()

    def enemy_fire_mission(self):
        """
        Generates computer shot.
        """
        y_column = random.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I"]).upper()
        x_row = random.randint(0, 8)
        return int(x_row) -1, GameBoard.co_ordinates()[y_column]
    
    def count_damaged_ships(self):
        damaged_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    damaged_ships +=1
        return damaged_ships

def run_game():
    """
    Main function. Will incorporate board and ship generation.
    """
    enemy_board = GameBoard([[" "] * 9 for i in range(9)])
    enemy_target_board = GameBoard([[" "] * 9 for i in range(9)])
    user_board = GameBoard([[" "] * 9 for i in range(9)])
    user_target_board = GameBoard([[" "] * 9 for i in range(9)])
    Warship.generate_fleet(enemy_board)
    Warship.generate_fleet(user_board)
    # turn counter
    missiles = 200
    while missiles > 0 :
        GameBoard.generate_board(user_target_board)
        GameBoard.generate_board(enemy_target_board)
        # get user input
        user_x_row, user_y_column = Warship.user_fire_mission(object)
        # checks if input is valid
        while user_target_board.board[user_x_row][user_y_column] == "-" or user_target_board.board[user_x_row][user_y_column] == "X":
            print("You have already fired on that location. Choose another.")
            user_x_row, user_y_column = Warship.user_fire_mission(object)
        # check for hit or miss
        if enemy_board.board[user_x_row][user_y_column] == "X":
            print("Direct hit! Enemy warship sunk!")
            user_target_board.board[user_x_row][user_y_column] = "X"
        else:
            print("Miss. No enemy warship at those co-ordinates.")
            user_target_board.board[user_x_row][user_y_column] = "-"
        # check victory condition
        if Warship.count_damaged_ships(user_target_board) == 5:
            print("Victory! The enemy fleet has been sunk!")
            break
        else:
            missiles -= 1
            print(f"You have {missiles} missiles remaining.")
            if missiles == 0:
                print("We are out of missiles. The enemy fleet has escaped.")
                GameBoard.generate_board(user_target_board)
        # get computer input
        enemy_x_row, enemy_y_column = Warship.enemy_fire_mission(object)
        while enemy_target_board.board[enemy_x_row][enemy_y_column] == "-" or enemy_target_board.board[enemy_x_row][enemy_y_column] == "X":
            enemy_x_row, enemy_y_column = Warship.enemy_fire_mission(object)
        # check for computer hit or miss
        if user_board.board[enemy_x_row][enemy_y_column] == "X":
            print("Direct hit! The enemy have sunk one of our ships!")
            enemy_target_board.board[enemy_x_row][enemy_y_column] = "X"
        else:
            print("The enemy have missed!")
            enemy_target_board.board[enemy_x_row][enemy_y_column] = "-"
        # check victory condition
        if Warship.count_damaged_ships(enemy_target_board) == 5:
            print("Retreat! The enemy have sunk our fleet!")
            break
        else:
            missiles -= 1
            if missiles == 0:
                print("The enemy have run out of missiles.")
                GameBoard.generate_board(enemy_target_board)


def game_over():
    """
    Runs when all ships sunk.
    Prompts user to restart or exit.
    """

def main():
    """
    Run all functions.
    """
    un_pw = login()
    check_login(un_pw)
    main_screen()
    run_game()

main()