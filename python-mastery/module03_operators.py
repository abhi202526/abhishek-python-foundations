# Operators 
# Arithmetic operators: +, -, *, /, //, %, **
# / is normal division, always gives a float (you just saw this: 7 / 2 = 3.5)
# // is floor division - division that throws away the decimal and rounds down: 7 // 2 = 3
# % is modulo - gives you the remainder after division: 7 % 2 = 1
# ** is exponent (power): 2 ** 3 = 8
# Comparison: ==, !=, > <, >= <=- these always return a bool (True/False)
# Logical: and or not- combine multiple True/False conditions

#. 1. Arithmetic Operators - doing math
a = 17
b = 5
print(a + b) # 22 -> addition
print(a - b) # 12 -> subtraction
print(a * b) # 85 -> multiplication
print(a / b) # 3.4 -> division - ALWAYS gives a float, even if it divides evenly
print(a // b) # 3 -> floor division - divides, then throws away the decimal (rounds DOWN)
print(a % b) # 2 -> modulo - gives you the REMAINDER after division
print(a ** b) # 1419857 -> exponent (power) - 17 to the power of 5

# 2. Comparison Operators - asking true/false questions
print(5 == 5) # True -> "is equal to" (TWO equals signs - very different from ONE)
print(5 != 3) # True -> "is NOT equal to"
print(5 > 3) # True -> greater than
print(5 < 3) # False -> less than
print(5 >= 5) # True -> greater than or equal to
print(5 <= 3) # False -> less than or equal to
# Every comparison operator always produces a bool- nothing else.

# 3. Logical Operators- combining multiple true/false checks
age = 20
is_student = True
print(age >= 18 and is_student)  # True AND True -> True
print(age >= 18 or is_student)   # only needs ONE to be True -> True
print(not is_student)            # flips True to False
# and -> both sides must be True for the whole thing to be True
# or -> only one side needs to be True
# not -> flips whatever follows it

# A subtlety worth knowing now, industry-relevant: Python checks and/or left to right, and stops early the moment it already knows the answer — this is called short-circuit evaluation. 
# Example:
age = 15
is_student = True
print(age >= 18 and is_student)

# Assignment Operators- shortcuts for updating a variable
score = 10    
score += 5 # same as: score = score + 5  -> score is now 15
score -= 3 # same as: score = score - 3  -> score is now 12
score *= 2 # same as: score = score * 2  -> score is now 24
score /= 4 # same as: score = score / 4  -> score is now 6.0

# Operator precedence- order of operations, same idea as math class
# Python follows the same "PEMDAS" rules you already know: ** first, then * / // %, then + -, and comparisons/logical operators last. When unsure, use parentheses () to make the order explicit — professional code favors clarity over relying on memorized precedence rules.


