'''Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)'''

# Ask user for a word
a = input("Please give me a word, and I will check if it is a palindrome.")
# Create a empty str, where we will insert the reverse string from the for loop
b = ""

# loop through string a and write to string b
for i in a:
    b = i + b

# Check if string a and b is equal
if a == b:
    print(a + " is a palindrome")
else:
     print(a + " is NOT a palindrome")   
