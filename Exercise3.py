'''Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.'''

# Aske user for input with a number to check against the list
check = int(input("Please give me a number I can check against my list? "))
# List to check number against
a = [1, 1, 2, 3, 5 ,8 ,12, 21, 34, 55 ,89]
# New empty list where we append all numbers less than users nubmer
b = []
# for loop where we loop through all elements in list a
for element in a:
    if element < check:
        b.append(element)
# Print out list b with all numbers less than the users number
print(b)


