# main.py

import display
import inputs
import routines


def main():
    while True:
        display.show_main_menu()

        choice = inputs.get_menu_choice(
            "Choose anq option: ", 1, 3
         )

        if choice is None:
            break

        if choice == 1:
            routines.run_calculator()

        elif choice == 2:
            routines.run_settings()

        elif choice == 3:
            display.show_info("Thank you for using the calculator!")
            break


if __name__ == "__main__":
    main()
