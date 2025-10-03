#!/usr/bin/env python3
# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.

# Loop until the user enters a positive integer
while True:
  user_response = input("How many terms of the Fibonacci sequence do you want? ")

# Checking if the input contains only numbers
if user_response.isdigit():
  terms = int(user_response) # Converting the input into an integer
  if terms > 0:
    break # If it's a valid input(positive integer) then exit the loop
  else:
    print("Please enter a positive integer.") # The input was either zero or negative
else:
  print("Please enter a positive integer.") # The input is not a number

# Initialize the first two numbers in the Fibonacci sequence
a = 0
b = 1

# Use a for loop to print the Fibonacci sequence up to that many terms.
for i in range(terms):
  print(a, end=" ") # Will print the current number with a space after
  a, b = b, a + b # Will update values following the Fibonacci sequence
