# prime
# Ibrahim El Hadi
# 02-11-2023
# Description: This program checks if the given number is prime or not

number = int(input("Enter a number to check if it's prime")) #prompt

is_prime = True # initsialise bolean

for i in range(2, number): # Loop from 2 up to the input number (as we don't need to check the number itself)
    if number % i == 0:  ## Check if the input number divided by the loop number has a remainder of 0 if the remainder is 0 it means that the input number is divisible by the current number in the loop
        is_prime = False # set bolean false
        break  # Break out of the loop if a factor is found

if is_prime: #if number is prime
    print(number, "is a prime number") #result
else:
    print(number, "is not a prime number") # if number not result




