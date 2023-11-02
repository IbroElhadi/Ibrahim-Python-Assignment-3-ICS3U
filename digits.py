# digits
# Ibrahim El Hadi
# 31-10-2023
# Description: This program takes a 4-digit, positive integer value and isolates each digit using integer division and remainder operations


number = int(input("Enter a 4-digit number between 1111 to 9999: ")) #prompt
if number >= 1111 and number <= 9999: #if statement
    thousands = number // 1000  #Gets number in thousandths
    hundreds = (number // 100) % 10#calculates hundreds by diving then remainder divided by 10
    tens = (number // 10) % 10#calculates hundreds by diving then remainder divided by 10
    ones = number % 10#calculates hundreds by finding numbers remainder divided by 10
    print("The digits of", number, "are", thousands, hundreds, tens, ones) #print the numbers
else:
    print("Invalid")
