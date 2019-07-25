from datetime import datetime
currentYear = datetime.now().year()
# Get the name from the user
name = input("What is your name? ")
# Get the age from the user
age = int(input("How old are you? "))
print(currentYear)

# Print out name, and calculate the year the user will turn 100
print(name + ", you will turn 100 years old in year " + str(2019 - age + 100))
