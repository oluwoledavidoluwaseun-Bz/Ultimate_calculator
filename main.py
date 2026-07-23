import math
print("Hello,world!")
# write a program to solve this equation
# 2x**2 + 2 10x + 12=0
# x**2 + 3x - 10= 0
# x**2 - (1/2)x - 5=0

# Reading Assignment 1 : Variable Naming Conventions

# Variable Naming Conventions 
# does she love me? [is in love] [fallen for me] 
# Lower Camel Case fallenForMe  | isInLove
# Upper Camel Case FallenForMe  | IsInLove
# Lower Snake Case fallen_for_me| is_in_love
# Upper Snake Case FALLEN_FOR_ME| IS_IN_LOVE

# Reading Assignment 2
# complete Lab 2.4.9 on the CISCO course

# Reading Assignment 4
# Read up Modules 2.6 and 3.1

# Assignment 3
# write a program to solve the following equations using the quadratic formula:
# 2x**2 + 10x + 12 = 0
# x**2 + 3x - 10 = 0
# x**2 - (1/2)x - 5 = 0
# (use the almighty formula)

#Assignment 3 answer
question_1 = "2x**2 + 10x + 12 = 0"
question_2 = "x**2 + 3x - 10 = 0"
question_3 = "x**2 - (1/2)x - 5 = 0"

a=2
b=10
c=12
calc_question_1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a) , (-b - (b**2 - 4*a*c)**0.5) / (2*a)
ans_question_1 = print(calc_question_1)
ans_question_1: None

a=1
b=3
c=-10
calc_question_2 = (-b + (b**2 - 4*a*c)**0.5) / (2*a), (-b - (b**2 - 4*a*c)**0.5) / (2*a)
ans_question_2 = print(calc_question_2)
ans_question_2: None

a=1
b=-0.5
c=-5
calc_question_3 = (-b + (b**2 - 4*a*c)**0.5) / (2*a), (-b - (b**2 - 4*a*c)**0.5) / (2*a)
ans_question_3 = print(calc_question_3)
ans_question_3: None

#Assignment Challenge
# build the following python program

# Welcome the the Quadratic Solver
# I solve everything your dull brain can't fathom in a quadratic equation
# If you don't like the insults take your assignment else where dullard!!!
#
# I hope you still remember this but your quadratic equation is of the form
# 
# ax**2 + bx + c = 0
#
# Enter a: 
# Enter b: 
# Enter c:
#
# x1 = ____ | x2 = ____

#Assignment Challenge answer
print("Welcome the the Quadratic Solver")
print("I solve everything your dull brain can't fathom in a quadratic equation\nIf you don't like the insults take your assignment else where dullard!!!")

print()
print("I hope you still remember this but your quadratic equation is of the form\n ax**2 + bx + c = 0")
print()

a= int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

print()

x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)

print(f"x1 = {x1} | x2 = {x2}")




#WEEK2 last class assignemts
# Reading assignment- 
# read uo f-strings
# build a simultaneeous equation
print("Welcome to the Simultaneous Equation Solver")

a=int(input("what is the coefficient of x in equ1? "))
b=int(input("what is the coefficient of y in equ1? "))
c= int(input("what is the value for c?"))

d=int(input("what is the coefficient of x in equ1? "))
e=int(input("what is the coefficient of y in equ1? "))
f= int(input("what is the value for f?"))

print(f"This is equ1- {a}x + {b}y = {c}")
print(f"This is equ2- {d}x + {e}y = {f}")
factor1 = int((c*e) - (f*b))
factor2 = int((a*e) - (f*b))
print ("since all variables have been filled i would solve for you now")
x = int(factor1 / factor2)
y = ((c - a*x) / b)

print(f"This is thw value for x: {x} and y{y}")
#end of simultanous equation solver

#simple calculator
print("Hello, welcome to your own personal calculator")
print("Note: its just a simple calculator so dont try anything complex and funny")

num1 = int(input("Enter first number: "))
print("The following are the symbols for each operation whiich you would need to specify")
print("Addition= + \n Division= / \n multiplication = * \n Subtraction= - \n floor division= // \n modulus=% \n Logerithm= log")
print()
op = input("Enter operator (+, -, *, /,//,%,log): ")
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
elif op == '//':
    if num2 == 0:
     print("Error: floor division by zero is not allowed.")
    elif num1== 0:
        print("Error: floor division by zero is not allowed.")
    else:
        print(f"Result: {num1} // {num2} = {num1 // num2}")
elif op == '%':
    if num2 == 0:
     print("Error: floor division by zero is not allowed.")
    else:
        print(f"Result: {num1} // {num2} = {num1 // num2}")
elif op == 'log':
    print(math.log(num1,num2))
else:
     print("Its not that complex just enter a valid operator😤")

#end of the simple calculator
#still needs work sha

#

