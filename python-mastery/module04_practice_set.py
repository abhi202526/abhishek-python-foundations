# Practice Set- Module 4

# 1. Ask the user for their name using input(), and print a greeting using an f-string: f"Hello, {name}!"

name = input("Enter your name: ")
print(f"Hello, {name}!")
# f stands for format string.

# 2. Ask for the user's age using input(), wrap the conversion in try/except ValueError, and print "You are old enough to vote" if age is 18 or above, otherwise "Not old enough yet"- but only if the conversion succeeds. If it fails, print and error message instead.

# Ask for input as a string first
age_input = input("What is your age: ")

try:
    # Try to convert the input to an integer
    age = int(age_input)

    # Check the voting age if conversion succeeds
    if age >= 18:
        print("You are old enough to vote")
    else:
        print("Not old enough yet")
except ValueError:
    # Handle the error if the user typed something that isn't a number
    print("Error: Please enter a valid number for your age.")

# 3. Deliberately break it- run your program from Question 2, and when it asks for age, type letters instead of numbers (like "twenty"). Paste me the real output showing your error message appeared instead of a crash.

age_input = input("What is your age: ")

try:
    age = int(age_input)

    if age >= 18:
        print("You are old enough to vote")
    else:
        print("Not old enough yet")
except ValueError:
    print("Error: Please enter a valid number for your age.")

# 4. Ask for two numbers using input() a (numerator / denominator), convert both to float inside a try block, and calculate numerator / denominator. Add a second except block sepcifically for ZeroDivisionError (a new error type- division by zero) in addition to your ValueError one. Test it three ways: valid numbers, non-numeric text, and a 0 denominator- paste all three real outputs.

numerator_input = input("Enter the numerator: ")
denominator_input = input("Enter the denominator: ")

try:
    # Convert inputs to float inside the try block
    num = float(numerator_input)
    den = float(denominator_input)

    # Calculate and print the result
    result = num / den
    print(f"Result: {result}")

except ValueError:
    # Handle text inputs that cannot be numbers
    print("Error: Please enter valid numbers only.")

except ZeroDivisionError:
    # Handle a denominator of 0 specifically
    print("Error: Cannot divide by zero.")

# 5. Genuinely tricky: What do you think happens if you write except (ValueError, ZeroDivisionError): as one line instead of two separate except blocks? Look this up in your own words or reason it out, then rewrite Quesiton 4 using this single combined version, and confirm it still handles both error types correctly.

numerator_input = input("Enter the numerator: ")
denominator_input = input("Enter the denominator: ")

try:
    # Convert inputs to float inside the try block
    num = float(numerator_input)
    den = float(denominator_input)

    # Calculate and print the result
    result = num / den
    print(f"Result: {result}")

except (ValueError, ZeroDivisionError):
    print("Error: Something went wrong with your input.")

    




