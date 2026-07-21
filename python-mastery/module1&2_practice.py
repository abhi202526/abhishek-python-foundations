# Practice Set- Modules 1&2 combined

# 1. Create variables for your name, age, height, and student status(all four types: str, int, float, bool). Print each with a label, then print each one's type().

name = "Abhishek"
age = 20
height = 5.10
age_float= 25.5
is_bool = True

print("Name:", name)
print("Age:", age)
print(f"Height: {height:.2f}")
print("Age (float):", age_float)
print("Is student:", is_bool)

# Understanding = vs assignment:

# 2. Predict, then run:
x = 10
x = x + 5
print(x)

# Dynamic typing:

# 3. Predict, then run:
value = 5
print(type(value))
value = "five"
print(type(value))

# Conversion edge cases:

# 4. Predict, then run- and explain in a comment why it fails:
# int("25.5") int() can only convert a string if it looks like a whole number, with absolutely nothing else in it.
# no decimal point, no letters, nothing. "25" works fine. "25.5" has a (.) in it, which int() simply doesn't know how to handle.

# 5. Predict, then run:
print(int(9.99)) # if we use int() function it chops off the decimal.

# Combining what you know- genuinely trickier:

# 6. Two variables: price = 499 (int) and discount = 0.1 (float, meaning 10%). Calculate the final price after discount (price - price * discount), print it, and print its type. Explain in a comment why the result is that type.
price = 499
discount = 0.1
pri_dis = price - price * discount
print(pri_dis)
print(type(pri_dis)) # the answer is in decimal so that's why the answer is in float.

# 7. 
name = "Abhishek"
age = 20
print(f"{name} is {age} years old.")

# 8. Debug this broken code (type it exactly as shown,run it,read the actual error message,then fix it):
name = "Abhishek"
print(name)