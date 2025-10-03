#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

# Validity of user input
valid = False

# Prompt user to input while given input is invalid
while not valid:
  try:
    # Asking user for the number of terms
    num_terms = int(input("Number of terms to print: "))

    if num_terms > 0:
      # Valid if number is positive
      valid = True
    else:
      # Error message if not positive
      print("Please enter a positive integer.")
  except:
    # Error message if input is not an int
    print("Please enter a positive integer.")

# Prepare fibonacci sequence
a = 0 # Current term
b = 1 # Next term

# Loop to print each term up until the given amount
for i in range(num_terms):
  # Print the current term
  print(a, end=" ")
  # Update next term
  a, b = b, a+b
  # a = b (current term is now the next term)
  # b = a + b (next is now current(previous) + next(current))
print()
