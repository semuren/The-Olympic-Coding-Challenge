'''Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.'''
import random
# Create an empty list. This will be used to generate a random list with numbers
numList = []
# Get length of list between 10 and 15 from randint
listLength = random.randint(10, 15)

# Use while loop to generate the random list (numList)
while len(numList) <= listLength:
    numList.append(random.randint(1, 99))




# Writes a for loop with an if, on one line. Returns the number from number in string a, if the number is even. 
b = [number for number in numList if number % 2 == 0]

# Get the odd numbers
c = [number for number in numList if number %  2 != 0]

# Print out the lists
print("Randomly generated list: " + str(numList))
print("Even numbers: " + str(b))
print("Odd numbers: " + str(c))
