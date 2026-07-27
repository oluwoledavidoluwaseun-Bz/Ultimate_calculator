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