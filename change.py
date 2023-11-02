# change
# Ibrahim El Hadi
# 01-11-2023
# Description: This program makes change using coins for a dollar amount less than $5.00

change = round(float(input("How much did you pay $0-$5")), 3)  # Prompt, round it to 3rd decimal
toonies = int(change // 2)  # find toonies by dividing
change %= 2  # return remainder of change and 2 repeat for rest
loonies = int(change // 1)
change %= 1
quarters = int(change // 0.25)
change %= 0.25
dimes = int(change // 0.1)
change %= 0.1
nickels = int(change // 0.05)
change %= 0.05
pennies = int(change // 0.01)

print(
    "You will receive",
    toonies,
    "Toonies,",
    loonies,
    "Loonies,",
    quarters,
    "Quarters,",
    dimes,
    "Dimes,",
    nickels,
    "Nickels, and",
    pennies,
    "Pennies.",
)  # Result
