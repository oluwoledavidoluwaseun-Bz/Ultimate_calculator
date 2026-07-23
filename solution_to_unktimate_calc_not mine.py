import math

def simple_calculator():
    print("\n--- Simple Calculator ---")
    print("Operations: +, -, *, /")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))
        
        if op == '+':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif op == '-':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif op == '*':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Invalid operator selected.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

def quadratic_solver():
    print("\n--- Quadratic Equation Solver ---")
    print("Form: ax^2 + bx + c = 0")
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        
        if a == 0:
            print("Coefficient 'a' cannot be zero in a quadratic equation.")
            return
            
        discriminant = b**2 - 4*a*c
        
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            print(f"Two real roots: x1 = {root1}, x2 = {root2}")
        elif discriminant == 0:
            root = -b / (2*a)
            print(f"One real root: x = {root}")
        else:
            real_part = -b / (2*a)
            imag_part = math.sqrt(-discriminant) / (2*a)
            print(f"Two complex roots: x1 = {real_part} + {imag_part}i, x2 = {real_part} - {imag_part}i")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

def simultaneous_solver():
    print("\n--- Simultaneous Linear Equations Solver ---")
    print("System form:\n  a1*x + b1*y = c1\n  a2*x + b2*y = c2")
    try:
        a1 = float(input("Enter a1: "))
        b1 = float(input("Enter b1: "))
        c1 = float(input("Enter c1: "))
        a2 = float(input("Enter a2: "))
        b2 = float(input("Enter b2: "))
        c2 = float(input("Enter c2: "))
        
        # Using Cramer's Rule determinant formula
        D = a1 * b2 - b1 * a2
        
        if D == 0:
            print("The system has no unique solution (lines are parallel or identical).")
        else:
            x = (c1 * b2 - b1 * c2) / D
            y = (a1 * c2 - c1 * a2) / D
            print(f"Solution: x = {x}, y = {y}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

def ultimate_calculator():
    while True:
        print("\n==============================")
        print("    THE ULTIMATE CALCULATOR   ")
        print("==============================")
        print("1. Quadratic Solver")
        print("2. Simultaneous Solver")
        print("3. Simple Calculator")
        print("4. Exit")
        
        choice = input("Pick an option (1-4): ").strip()
        
        if choice == '1':
            quadratic_solver()
        elif choice == '2':
            simultaneous_solver()
        elif choice == '3':
            simple_calculator()
        elif choice == '4':
            print("\nThank you for using the Ultimate Calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please pick a valid option between 1 and 4.")

# Launch the program
if __name__ == "__main__":
    ultimate_calculator()
