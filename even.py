# even
# Ibrahim El Hadi
# 02-11-2023
# Description: This program checks if the given number is even or not

number = int(input("Enter a number to check if it's even: "))  # prompt

if number % 2 == 0:  # Check if the number leaves no remainder when divided by 2
    print(number, "is an even number")  # result
else:
    print(number, "is not an even number")
