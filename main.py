import random

print("Welcome to Elijah's random number picker!")
print("Please enter two numbers below (like one and ten) so the code can choose a number between them:")

number_one = int(input("What is the first number? ")
number_two = int(input("What is the second number? ")
                 
result = random.randint(number_one, number_two)
print(f"The chosen number is:", result)
print("Copyright (c) 2025 Elijah Corwin")
