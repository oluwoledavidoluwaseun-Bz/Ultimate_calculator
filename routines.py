# modules/routines.py

import arithmetic, display, inputs, state

OPERATIONS = {
    1: ("+", arithmetic.add),
    2: ("-", arithmetic.sub),
    3: ("*", arithmetic.mul),
    4: ("/", arithmetic.div),
    5: ("//", arithmetic.floordiv),
    6: ("%", arithmetic.mod),
    7: ("**", arithmetic.exp),
    8: ("pow", arithmetic.power),
    9: ("log", arithmetic.log),
}


def run_calculator():
    while True:
        display.show_arithmetic_menu()

        choice = inputs.get_menu_choice("Choose operation: ", 1, 10)
        if choice in (None, 10):
            return

        num1 = inputs.get_number("First number: ")
        num2 = inputs.get_number("Second number: ")
        if num1 is None or num2 is None:
            return

        symbol, func = OPERATIONS[choice]

        try:
            result = func(num1, num2)
            display.show_calculation(
                num1,
                num2,
                symbol,
                result,
                state.get_decimal_places()
            )
        except Exception as e:
            display.show_error(str(e))

        display.show_rerun_menu()
        if inputs.get_yes_no("Again? (1=Yes, 2=No): ") is not True:
            break


def run_settings():
    while True:
        display.show_settings_menu()

        choice = inputs.get_menu_choice("Choose option: ", 1, 3)

        if choice in (None, 3):
            return

        if choice == 1:
            display.show_info(
                f"Decimal places: {state.get_decimal_places()}"
            )
        else:
            dp = inputs.get_decimal_places()
            if dp is not None:
                state.set_decimal_places(dp)
                display.show_success("Settings updated.")