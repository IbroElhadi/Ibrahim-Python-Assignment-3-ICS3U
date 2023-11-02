# fraction
# Ibrahim El Hadi
# 02-11-2023
# Description: This program converts a fraction from improper form to mixed form

numerator = int(input("Enter the numerator: ")) #prompts
denominator = int(input("Enter the denominator: "))

whole = numerator // denominator
remainder = numerator % denominator #Calculate the remainder as the part not evenly divisible by the denominator

print(numerator, "/", denominator, "is equivalent to", whole, "and", remainder, "/", denominator) #maths
