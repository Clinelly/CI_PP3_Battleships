# Elements of this code were inspired by Knowledge Mavens on YouTube
# (https://www.youtube.com/watch?v=alJH_c9t4zw&t=673s)
# Code elements were modified for additional functionality.

# imports the inbuilt python random module
import random
# imports login.py file
import login

# imports google spreadhseet and google credentials APIs
import gspread
from google.oauth2.service_account import Credentials

# Global variables assigned to allow access through Google APIs to gspread.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("user_data_sheet")


def main_screen():
    """
    A function to generate the main screen before the game starts.
    ASCII art dashboard and asks player to start game.
    """

    print("                                  # #  ( )")
    print("                               ___#_#___|__")
    print("                           _  |____________|  _")
    print("                    _=====| | |            | | |==== _")
    print("              =====| |.---------------------------. | |====")
    print("<--------------------'   .  .  .  .  .  .  .  .   '--------------/")
    print("  \                                                             /")
    print("   \___________________________________________________________/")

    print("         _ __        _   _   _           _     _   ")
    print("        |  _ \      | | | | | |         | |   (_) ")
    print("        | |_)/  __ _| |_| |_| | ___  ___| |__  _ _ __   ___ ")
    print("        | '_ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \ / __| ")
    print("        | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |\__ \ ")
    print("        |_.__/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ |___/ ")
    print("                                                | |   ")
    print("                                                |_| ")


class GameBoard:
    """
    Stores the values needed to generate the game board.
    Dictionary stores letter/number values for co-ordinates.
    Stores values for a board outline for user visuals.
    """

    def __init__(self, board):
        self.board = board

    def co_ordinates():
        co_ordinates = {
            "A": 0,
            "B": 1,
            "C": 2,
            "D": 3,
            "E": 4,
            "F": 5,
            "G": 6,
            "H": 7,
            "I": 8,
        }
        return co_ordinates

    def generate_board(self):
        print("  A B C D E F G H I ")
        print("  x-x-x-x-x-x-x-x-x ")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class Warship:
    """
    Class that stores the values needed to generate the ships.
    """

    def __init__(self, board):
        self.board = board

    def generate_fleet(self):
        """
        For statement loops through the board co-ordinate lists.
        Generates random integers and assigns 'X' as a ship to each.
        Integers translated into co-ordinates and a ship is placed.
        """
        for i in range(8):
            self.x_row, self.y_col = random.randint(0, 8), random.randint(0, 8)
            while self.board[self.x_row][self.y_col] == "X":
                self.x_row = random.randint(0, 8)
                self.y_col = random.randint(0, 8)
            self.board[self.x_row][self.y_col] = "X"
        return self.board

    def user_fire_mission(self):
        """
        Takes the user input and checks for validation.
        Assigns the shot to a co-ordinate and checks for hit/miss/sink.
        Feeds back to user.
        """
        try:
            y_col = input("Enter Co-Ordinate (A-I): ").upper()
            if y_col:
                while y_col not in "ABCDEFGHI":
                    print("Invalid co-ordinate. Enter a letter A-I.")
                    y_col = input("Enter Co-Ordinate (A-I): ").upper()
            else:
                print("Empty Input. Enter a letter A-I.")
                y_col = input("Enter Co-Ordinate (A-I): ").upper()
            x_row = input("Enter Co-Ordinate (1-9): ")
            if x_row:
                while x_row not in "123456789":
                    print("Invalid co-ordinate. Enter a number 1-9.")
                    x_row = input("Enter Co-Ordinate (1-9): ")
                return int(x_row) - 1, GameBoard.co_ordinates()[y_col]
            else:
                print("Empty Input. Enter a number 1-9.")
                x_row = input("Enter Co-Ordinate (1-9): ")
        except ValueError and KeyError:
            print("Not a valid input. Enter a letter or a number.")
            return self.user_fire_mission()

    def enemy_fire_mission(self):
        """
        Generates computer shot.
        Takes co-ordinates from a random choice of letters and integers.
        """
        y_col = random.choice([
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I"
        ]).upper()
        x_row = random.randint(0, 8)
        return int(x_row) - 1, GameBoard.co_ordinates()[y_col]

    def count_damaged_ships(self):
        damaged_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    damaged_ships += 1
        return damaged_ships


def run_game():
    """
    Main function.
    Generates board and ships.
    Incorporates a turn limit.
    Prompts user for input and provides feedback on turn results.
    """
    enemy_board = GameBoard([[" "] * 9 for i in range(9)])
    enemy_target_board = GameBoard([[" "] * 9 for i in range(9)])
    user_board = GameBoard([[" "] * 9 for i in range(9)])
    user_target_board = GameBoard([[" "] * 9 for i in range(9)])
    Warship.generate_fleet(enemy_board)
    Warship.generate_fleet(user_board)
    # turn counter
    missiles = 32
    enemy_missiles = 32
    while missiles > 0:
        GameBoard.generate_board(user_target_board)
        GameBoard.generate_board(enemy_target_board)
        # get user input
        user_x_row, user_y_col = Warship.user_fire_mission(object)
        # checks if input is valid
        while (
            user_target_board.board[user_x_row][user_y_col] == "-"
            or user_target_board.board[user_x_row][user_y_col] == "X"
        ):
            print("You have already fired on that location. Choose another.")
            user_x_row, user_y_col = Warship.user_fire_mission(object)
        # check for hit or miss
        if enemy_board.board[user_x_row][user_y_col] == "X":
            print("Direct hit! Enemy warship sunk!")
            user_target_board.board[user_x_row][user_y_col] = "X"
        else:
            print("Miss. No enemy warship at those co-ordinates.")
            user_target_board.board[user_x_row][user_y_col] = "-"
        # check victory condition
        if Warship.count_damaged_ships(user_target_board) == 8:
            print("Victory! The enemy fleet has been sunk!")
            break
        else:
            missiles -= 1
            print(f"You have {missiles} missiles remaining.")
            if missiles == 0:
                print("We are out of missiles. The enemy fleet has escaped.")
                GameBoard.generate_board(user_target_board)
        # get computer input
        enemy_x_row, enemy_y_col = Warship.enemy_fire_mission(object)
        while (
            enemy_target_board.board[enemy_x_row][enemy_y_col] == "-"
            or enemy_target_board.board[enemy_x_row][enemy_y_col] == "X"
        ):
            enemy_x_row, enemy_y_col = Warship.enemy_fire_mission(object)
        # check for computer hit or miss
        if user_board.board[enemy_x_row][enemy_y_col] == "X":
            print("Direct hit! The enemy have sunk one of our ships!")
            enemy_target_board.board[enemy_x_row][enemy_y_col] = "X"
        else:
            print("The enemy have missed!")
            enemy_target_board.board[enemy_x_row][enemy_y_col] = "-"
        # check victory condition
        if Warship.count_damaged_ships(enemy_target_board) == 8:
            print("Retreat! The enemy have sunk our fleet!")
            break
        else:
            enemy_missiles -= 1
            if missiles == 0:
                print("The enemy have run out of missiles.")
                GameBoard.generate_board(enemy_target_board)
    game_over()


def game_over() -> str:
    """
    Runs when all ships sunk.
    Prompts user to restart or exit.
    """
    print("GAME OVER")
    retry = input("Would you like to play again? Y/N: \n").lower()

    if str(retry) == 'y':
        run_game()
    elif str(retry) == 'n':
        print("Thank you Admiral. You are relieved of your command.")
        quit()
    elif str(retry) not in {"y", "n"}:
        print("Invalid Input. Type in Y/N.")
        game_over()


def main():
    """
    Run all functions.
    """
    #new_old = login.login()
    #login.check_login(new_old)
    main_screen()
    run_game()


main()

if __name__ == "__main__":
    main()
