# modules/routines.py

import arithmetic, display, inputs, state

OPERATIONS = {
    1: ("+", arithmetic.add, 2),
    2: ("-", arithmetic.sub, 2),
    3: ("*", arithmetic.mul, 2),
    4: ("/", arithmetic.div, 2),
    5: ("//", arithmetic.floordiv, 2),
    6: ("%", arithmetic.mod, 2),
    7: ("e^", arithmetic.exp, 1),
    8: ("pow", arithmetic.power, 2),
    9: ("log", arithmetic.log, 2),
}


def get_operands(operand_count):
    """
    Gets num1 (and num2, if needed), offering to reuse the previous result first.
    Returns (num1, num2) - num2 will be None for single-operand operations.
    Returns None if the user quits partway through.
    """
    num1 = None
    num2 = None
    previous = state.get_previous_result()

    if previous is not None:
        display.show_info(f"Previous result available: {previous}")
        reuse = inputs.get_yes_no("Reuse previous result? (1=Yes, 2=No): ")
        if reuse is None:
            return None

        state.set_reuse_result(reuse)

        if reuse:
            if operand_count == 1:
                # only one slot to fill, so the previous result goes straight in
                num1 = previous
            else:
                which = inputs.get_menu_choice(
                    "Use previous result as num1 or num2? (1=num1, 2=num2): ", 1, 2
                )
                if which is None:
                    return None
                if which == 1:
                    num1 = previous
                else:
                    num2 = previous

    if num1 is None:
        num1 = inputs.get_number("First number: ")
        if num1 is None:
            return None

    if operand_count == 2 and num2 is None:
        num2 = inputs.get_number("Second number: ")
        if num2 is None:
            return None

    return (num1, num2)


def run_calculator():
    while True:
        display.show_arithmetic_menu()

        choice = inputs.get_menu_choice("Choose operation: ", 1, 10)
        if choice in (None, 10):
            return

        symbol, func, operand_count = OPERATIONS[choice]

        operands = get_operands(operand_count)
        if operands is None:
            return

        num1, num2 = operands

        try:
            if operand_count == 2:
                result = func(num1, num2)
            else:
                result = func(num1)

            display.show_calculation(
                num1,
                num2 if num2 is not None else 0,
                symbol,
                result,
                state.get_decimal_places()
            )
            state.set_previous_result(result)
            state.set_current_operation(symbol, num1, num2)
        except Exception as e:
            display.show_error(str(e))

        display.show_rerun_menu()
        if inputs.get_yes_no("Again? (1=Yes, 2=No): ") is not True:
            break

run_calculator()
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
            display.show_info(f"Current decimal places: {state.get_decimal_places()}")
            dp = inputs.get_decimal_places()
            if dp is not None:
                state.set_decimal_places(dp)
                display.show_success(f"Decimal places updated to {state.get_decimal_places()}")