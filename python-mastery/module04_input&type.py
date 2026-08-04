# Input & Type Conversion, Safely:

# input()- asking the user a question
name = input("What is your name? ")
print("Hello,", name)

# input() always returns a string, no matter what the person types.

# Why raw conversion is fragile
age = input("Enter your age: ")
age = int(age)  # what if they type "twenty" instead of "20"? : instant error
print(age)

# The fix: wrap conversion in try/except

age_input = input("Enter your age: ")

try:
    age = int(age_input)
    print("Your age is:", age)
except ValueError:
    print("That's not a valid whole number. Please enter digits only.")

# Looping until you get valid input- a genuinely useful pattern

# Right now, if the input is bad, our program just prints an error and moves on. Often, you actually want to keep asking until the person gives something valid. We haven't covered loops yet(Module 6), so for now, just know this pattern exists- we'll build it properly once loops are in your toolkit:

# Preview only- We'll build this for real in Module 6
while True:
    age_input = input("Enter your age: ")
    try:
        age = int(age_input)
        break
    except ValueError:
        print("Invalid input, try again.")

# Multiple conversions, multiple risks

hours = input("Enter hours worked: ")
rate = input("Enter hourly rate: ")

try:
    hours = float(hours)
    rate = float(rate)
    pay = hours * rate
    print("Total pay:", pay)
except ValueError:
    print("Please enter valid numbers for both hours and rate.")
