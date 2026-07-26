# state.py

state = {"previous_result": None, "reuse_result": False, "current_operation": None,   # e.g. "add", "sub", "div"
    "num1": None,
    "num2": None}

config = {"decimal_places": 2}

def set_previous_result(value) -> None:
    state["previous_result"] = value

def get_previous_result():
    return state["previous_result"]

def get_decimal_places() -> int:
    return config["decimal_places"]

def set_decimal_places(value: int) -> bool:
    if 0 <= value <= 9:
        config["decimal_places"] = value
        return True
    else:
        return False