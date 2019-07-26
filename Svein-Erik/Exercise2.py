# Odd or Even

# Use input to get a number(int) from user
num1 = int(input("Give me a number, and I will check if it is even or odd: "))

# To check if it is even, we check if the number is dividable with 2 or not 
# Check if number is a multiple of 4
if num1 % 4 == 0:
    print(str(num1) + " is a multiple of 4")
# if not multiple of 4, check if number is even
elif num1 % 2 == 0:
    print(str(num1) + " is an even number")
# if number is not multiple of 4, or even it is an odd number
else:
    print(str(num1) + " is an odd number")
    
# Extra: Check if two numbers are dividable
num2 = int(input("Check if to numbers are dividable. Give me a number:"))
check = int(input("What number do you want to check against?"))

if num2 % check == 0:
    print(str(num2) + " is dividable with " + str(check))
else:
    print(str(num2) + " is not dividable with " + str(check))
