# round
# Ibrahim El Hadi
# 02-11-2023
# Description: This program rounds a number to a specified number of decimal places

# Initialize the values
number = float(input("Enter the number you want to round;"))#prompts
decimal_places = int(input("Enter the number of decimal places:"))

roundedNumber = round(number * (10 ** decimal_places)) / (10 ** decimal_places)#calculate rounded number

print("The rounded number is:", roundedNumber)#result