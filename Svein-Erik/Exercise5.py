'''Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)'''
import random

# Make two random lists. Range of the numbers inside the list will be from 1 to 30. List length will be from 5 to 20 items.
a = random.sample(range(30), random.randint(5, 20))
b = random.sample(range(30), random.randint(5, 20))

# New list where we will append the common elements from each list
c = []

# Loop through list a and b to find common elements, and add them to list c
for n in a and b:
    if n in a and b:
        c.append(n)
 
# Print the two random lists we made on line 14 and 15
print("List a: " + str(a))
print("List b: "+ str(b))  
# Print the new list we made with common elements. 
print("List a and b have following elements in common:")
print(str(c) + "\n")
