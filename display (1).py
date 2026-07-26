def show_main_menu():
    print(f"===== 📅 Calculator Menu =====")
    print("1. Calculator 📠")
    print("2. Settings ⚙️")
    print("3. Exit 🚫")
    print(f"===== 📅 Calculator Menu =====")

def show_arithmetic_menu():
    print("===== 📅 Arithmetic Menu =====")
    print("1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")
    print("5. FloorDiv")
    print("6. Mod")
    print("7. Exp")
    print("8. Pow")
    print("9. Log")
    print("10. Return")
    print("===== 📅 Arithmetic Menu =====")

def show_settings_menu():
    print("===== 📅 Settings Menu =====")
    print("1. View current settings")
    print("2. Edit settings")
    print("3. Return to main menu")
    print("===== 📅 Settings Menu =====")

def show_rerun_menu():
    print("===== 📅 Rerun Calculator Menu =====")
    print("1. Yes")
    print("2. No")
    print("===== 📅 Rerun Calculator Menu =====")

def format_number(number, decimal_places):
    return f"{number:.{decimal_places}f}"

def show_calculation(num1, num2, operator_symbol, result, decimal_places):
    print(f"num1 = {format_number(num1, decimal_places)}")
    print(f"num2 = {format_number(num2, decimal_places)}")

    if result is None:
        print(f"num1 {operator_symbol} num2 =")
    else:
        print(f"num1 {operator_symbol} num2 = {format_number(result, decimal_places)}")

def show_info(message):
    print(f"ℹ️ Message: {message}")

def show_warning(message):
    print(f" ⚠️ Warning: {message}")

def show_error(message):
    print(f"🚫 Error: {message}")

def show_success(message):
    print(f"✅ Success: {message} ")

if __name__ == "__main__":
    show_calculation(0, 0, "+", None, 2)
    print()
    show_calculation(15, 25, "+", 40, 2)
    show_main_menu()
    show_arithmetic_menu()
    show_settings_menu()
    show_rerun_menu()
    print(format_number(15, 2))