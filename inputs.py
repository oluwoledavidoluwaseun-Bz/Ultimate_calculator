num1 = input("Enter num1: ")
# num1 is a str


# Reading Assignment 2 
# - Write code to convert num1 from a str to a float without triggering a ValueError
# - Do not use try-except (YES I'm that wicked)

num1 = input("Enter a number: ")

# remove a leading minus sign (if any) so we can check the rest
check = num1
if check.startswith('-'):
    check = check[1:]

# remove one decimal point (if any) so we can check the rest
check = check.replace('.', '', 1)

# now check is only digits if the original was a valid number
if check.isdigit():
    num1 = float(num1)
    print("Converted number:", num1)
else:
    print("That is not a valid number.")