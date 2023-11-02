# diamond
# Ibrahim El Hadi
# 02-11-2023
# Description: Diamond

height = int(input("What is your desired height of diamond"))  #prompt


for i in range(1, height + 1, 2):# This loop generates the upper half of the diamond.
    # It starts at 1 and increments by 2 in each iteration, ensuring that only odd numbers are generated.
    # The loop continues until it reaches the desired height.
    # This is done to create the diamond shape effectively, as adding 2 in each step ensures balanced growth of asterisks on both sides.
    # The filler variable calculates the number of spaces needed to center the asterisks properly.
    filler = " " * ((height - i) // 2)  # Calculate the number of spaces needed
    print(filler + "*" * i)  # Print the string as needed

for i in range(height - 2, 0, -2): # same as top but going down
    filler = " " * ((height - i) // 2)
    print(filler + "*" * i)
