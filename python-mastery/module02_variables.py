# Module 2: Variables & Data Types

# The core data types
# Type	       Holds	                                         Example	         type() shows
# int	   whole numbers, positive or negative	                age = 20	         <class 'int'>
# float	   decimal numbers	                                    price = 99.5	     <class 'float'>
# str	   text, always quoted  	                            name = "Abhishek"	 <class 'str'>
# bool	   only True or False (capital letters, no quotes)	    is_active = True	 <class 'bool'>

# Checking a variable's type:
age = 20
print(type(age))

# Type Conversion - changing one type into another, deliberately
int("25")
float("25.5")
str(25)

# Two things that will fail, and why:
int("hello") # crashes - "hello" isn't a valid number, no way to convert it
int(3.9) # works, but truncates (doesn't round!) gives 3, not 4

name = "Abhishek"
age = 20
height = 5.10
is_student = True

print("Name:", name)
print("Age:", age)
print(f"Height: {height:.2f}") # f-string(formatted string)- the f before the quotes lets you drop variables directly inside ({}), and (:.2f) specifically means "show this as a decimal number, with exactly 2 digits after the point."
print("Is student:", is_student)

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

total = age + height
print(total)
print(type(total))

x = 7
y = 2
print(x / y)
print(type(x / y))


