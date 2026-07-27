# input page
# inputs.py
from display import show_info, show_warning, show_error
QUIT_WORDS = ("quit", "q", "exit", "e")


# This function: Displays a reminder to the user that they can cancel
# the current operation by typing "quit, q, exit or e."
def quit_message():
    show_info(" Enter (quit/q/exit/e) to cancel current operation")


# This function: Checks whether the user's input is a quit command
# and returns True if it is, otherwise False.
def is_quit(user_input):
    return user_input.lower() in QUIT_WORDS


# This function: Accepts and validates the user's menu selection,
# ensuring it is within the specified range before returning it.
def get_menu_choice(prompt, min_choice, max_choice):
    """
    Gets and validates menu input.
    Returns None if user quits.
    """

    while True:
        quit_message()

        choice = input(prompt).strip()

        if is_quit(choice):
            show_warning( "Operation cancelled.")
            return None

        if choice.isdigit():
            choice = int(choice)

            if min_choice <= choice <= max_choice:
                return choice

        show_error("Invalid menu selection.")


# Function for Number Input
# This function: Accepts and validates numerical input,
# ensuring the user enters a valid number before returning it.
def get_number(prompt):
    """
    Gets a valid number from the user.
    Returns None if user quits.
    """

    while True:
        quit_message()

        value = input(prompt).strip()

        if is_quit(value):
            show_warning( "Operation cancelled.")
            return None

        try:
            return float(value)

        except ValueError:
            show_error("User response is not a number.")


# Function for Yes/No Question
# This function: Accepts a Yes/No choice from the user
# (1 for Yes, 2 for No) and returns the corresponding
# Boolean value (True or False).
def get_yes_no(prompt):
    """
    Returns True for Yes.
    Returns False for No.
    """

    while True:
        quit_message()

        choice = input(prompt).strip()

        if is_quit(choice):
            show_warning("Operation cancelled.")
            return None

        if choice == "1":
            return True

        if choice == "2":
            return False

        show_error("Invalid choice. Choose 1 or 2.")


# Function For Decimal Places
# This function: Accepts and validates the number of decimal places
# (0–9) that the user wants for displaying calculation results.
def get_decimal_places():
    """
    Gets and validates decimal places.
    Returns None if user quits.
    """

    while True:
        quit_message()

        value = input("Enter decimal places (0-9): ").strip()

        if is_quit(value):
            show_warning("Operation cancelled.")
            return None

        if value.isdigit():
            value = int(value)

            if 0 <= value <= 9:
                return value

        show_error("Decimal places must be between 0 and 9.")