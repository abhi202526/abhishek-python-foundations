# # Practice Set- Module 5

# # 1. Write a grading program: ask for marks via input() (converted safely with try/except), and use if/elif/else to print a grade- A(90+), B(75-89), C(50-74), F(below 50). Test with a score that should land in each of the four categories(four separate runs). 

marks_input = input("Enter your marks: ")

try:
    marks = int(marks_input)

    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 50:
        print("Grade C")
    else:
        print("Grade F")

except ValueError:
    print("Error: Please  enter a valid number for your marks.")

# 2. Order-matters test- deliberately write your elif conditions in the wrong order (smallest threshold first, like marks >= 50 before marks >= 90), run it with marks = 95, and paste me the (wrong) result. Then fix the order and confirm it's correct. This is meant to make you see the bug, not just be told about it.
# Using input() function:
marks_input = input("Enter your marks: ")

try:
    marks = int(marks_input)

    if marks >= 50:
        print("Grade C")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 90:
        print("Grade A")
    else: 
        print("Grade F")

except ValueError: 
    print("Error: Please enter a valid number for your marks.")

# Without using input() function:
marks = 95

if marks >= 50:
    print("Grade C")
elif marks >= 75:
    print("Grade B")
elif marks >= 90:
    print("Grade A")
else: 
    print("Grade F")

# 3. Nested conditional: write a simple login check- ask for a username and password via input(). First check if the username equals "admin" (exactly), and only if that's true, nest a second check for whether the password equals "1234". Print different messages for: correct username + correct password, correct username + wrong password, and wrong username entirely.

user_name = input("Enter your username: ")

if user_name == "admin":
    pass_word = input("Enter you password: ")

    if pass_word == "1234":
        print("correct username + correct password")
    else:
        print("correct username + wrong password")
else:
    print("wrong username entirely")

# 4. Truthy/falsy- if user_input: with no == comparison, tested both with real input and an empty Enter press.

user_input = input("Enter something (or just press Enter): ")

if user_input:
    print("You entered something")
else:
    print("You entered nothing")