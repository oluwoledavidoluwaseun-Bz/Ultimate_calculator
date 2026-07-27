# input page
# inputs.py
from display import show_info

QUIT_WORDS = ("quit", "q", "exit", "e")


def quit_message():
    show_info(" Enter (quit/q/exit/e) to cancel current operation")


# Function to return whatever user input and change to small letters and if it is in the quit words list then return True
def is_quit(user_input):
    return user_input.lower() in QUIT_WORDS


def get_menu_choice(prompt, min_choice, max_choice):
    """
    Gets and validates menu input.
    Returns None if user quits.
    """

    while True:
        quit_message()

        choice = input(prompt).strip()

        if is_quit(choice):
            print("⚠️ Operation cancelled.")
            return None

        if choice.isdigit():
            choice = int(choice)

            if min_choice <= choice <= max_choice:
                return choice

        print("🚫 Error: Invalid menu selection.")

        # Function for Number Input

        def get_number(prompt):
          """
           Gets a valid number from the user.
          """

          while True:
           quit_message()

        value = input(prompt).strip()

        if is_quit(value):
            print("⚠️ Operation cancelled.")
            return None

        try:
            return float(value)

        except ValueError:
            print("🚫 Error: user response is not a number")
# Function for Yes/No Question

def get_yes_no(prompt):
    """
    Returns True for Yes.
    Returns False for No.
    """

    while True:
        quit_message()

        choice = input(prompt).strip()

        if is_quit(choice):
            print("⚠️ Operation cancelled.")
            return None

        if choice == "1":
            return True

        if choice == "2":
            return False

        print("🚫 Error: Choose 1 or 2.")
# Function For Decimal Places

def get_decimal_places():
    while True:
        quit_message()

        value = input("Enter decimal places (0-9): ").strip()

        if is_quit(value):
            print("⚠️ Operation cancelled.")
            return None

        if value.isdigit():
            value = int(value)

            if 0 <= value <= 9:
                return value

        print("🚫 Error: Decimal places must be between 0 and 9.")