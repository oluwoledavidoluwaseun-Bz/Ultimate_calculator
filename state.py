# modules/state.py

# Stores the calculator settings

_decimal_places = 2


def get_decimal_places():
    """
    Returns the current number of decimal places.
    """
    return _decimal_places


def set_decimal_places(value):
    """
    Updates the decimal places.
    """
    global _decimal_places

    if not isinstance(value, int):
        raise TypeError("Decimal places must be an integer.")

    if value < 0:
        raise ValueError("Decimal places cannot be negative.")

    _decimal_places = value


def get_settings():
    """
    Returns all current settings as a dictionary.
    """
    return {
        "decimal_places": _decimal_places
    }


def reset_settings():
    """
    Restores the default settings.
    """
    global _decimal_places
    _decimal_places = 2

# ---- Previous result / reuse tracking ----    

_previous_result = None
_reuse_result = False
_current_operation = None


def get_previous_result():
    """
    Returns the result of the last calculation, or None if there isn't one yet.
    """
    return _previous_result


def set_previous_result(value):
    """
    Stores the result of the most recent calculation.
    """
    global _previous_result
    _previous_result = value


def get_reuse_result():
    """
    Returns True/False depending on whether the user chose to reuse the previous result.
    """
    return _reuse_result


def set_reuse_result(value):
    """
    Records whether the user wants to reuse the previous result.
    """
    global _reuse_result
    _reuse_result = value


def get_current_operation():
    """
    Returns the operation currently being worked on, as (symbol, num1, num2).
    """
    return _current_operation


def set_current_operation(symbol, num1, num2):
    """
    Stores the operation and operands currently being worked on.
    """
    global _current_operation
    _current_operation = (symbol, num1, num2)
