# Conditionals- if/elif/else
# The basic shape
age = 20

if age >= 18:
    print("You are an adult")

# Adding else- the "otherwise" case
age = 15

if age >= 18:
    print("You are an adult")

else: 
    print("You are a minor")

# elif- Checking multiple conditions in sequence (the genuinely new part)

marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else: 
    print("Grade: F")

# The critical thing to understand- order matters, and Python stops at the first match: Python checks these top to bottom, and the moment one condition is True, if runs that block and skips every other elif/else below it entirely- even if a later condition would also technically be true.

# Nested conditionals- an if inside another if
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Entry denied- no ID")
else:
    print("Entry denied- underage")

# Truthy and Falsy- a genuinely important, slightly advanced idea

# In Python, if doesn't only work with True/False directly — it can check almost any value, because Python automatically treats certain values as meaning "false-like" even if they're not the actual word False:
name = " "
if name:
    print("Name provided")
else: 
    print("Name is empty")