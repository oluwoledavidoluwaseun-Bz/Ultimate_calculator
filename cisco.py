# co=int(input("input value: "))

# steps =0
# while True:
#     co_even= co%2
#     if co != 1:
#         if co_even == 0:
#             co = co//2
#             print (co)
#         else:
#             co = 3 *co + 1
#             print (co)
#     else:
#         break
#     steps += 1

# print(f"steps are: {steps}")


text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")

