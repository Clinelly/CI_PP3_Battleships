# imports the inbuilt python random module
import random

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
        new_old = input("Are you a new user? Y/N \n").lower()

        if str(new_old) == "y":
            new_user()
        else:
            old_user()

        if check_login(new_old):
            break
    return new_old


def check_login(un_pw):
    """
    Checks user input is acceptable.
    Raises ValueError if not.
    """
    try:
        str(un_pw)
        if un_pw not in ["y", "n"]:
            raise ValueError("Invalid Input.")
    except ValueError as e:
        print(f"{e} Please type in Y or N.")
        return False

    return True


def new_user():
    """
    Prompts user to choose their username and password.
    Takes user input and stores them in the google spreadsheet.
    """
    un_login = SHEET.worksheet("username")
    pw_login = SHEET.worksheet("password")
    new_un = input("Enter a username:\n")
    un_lst = str.split(new_un)
    un_login.append_row(un_lst)
    print(f"Welcome Admiral {new_un}")
    new_pw = input("Enter a password:\n")
    pw_lst = str.split(new_pw)
    pw_login.append_row(pw_lst)
    print("Password stored.")


def old_user():
    """
    Prompts a returning user to enter their username and password.
    Checks user input against values stored in the spreadsheet.
    Invalid inputs cause users to return to login step.

    """
    un_login = SHEET.worksheet("username")
    pw_login = SHEET.worksheet("password")
    old_un = input("Enter your username:\n")
    check_un = un_login.find(old_un)
    if check_un is None:
        print("Username not found. Check your credentials and try again.")
        login()
    else:
        print(f"Welcome back Admiral {old_un}.")
    old_pw = input("Enter your password:\n")
    check_pw = pw_login.find(old_pw)
    if check_pw is None:
        print("Password invalid. Check your credentials and try again.")
        login()
    else:
        print("Password verified.")


def main():
    """
    Run all functions.
    """
    new_old = login()
    check_login(new_old)


main()
