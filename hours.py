# hours
# Ibrahim El Hadi
# 31-10-2023
# Description: This program takes a time interval in hours, minutes, and seconds and converts it to hours using mathematical operations


hours = int(input("Enter the number of hours")) # prompt
minutes = int(input("Enter the number of minutes")) #prompt
seconds = int(input("Enter the number of seconds")) #prompt

total = hours + (minutes / 60) + (seconds / 3600) #do the math

print(hours, "hours", minutes, "minutes", seconds, "seconds is ", total, "hours") #print result