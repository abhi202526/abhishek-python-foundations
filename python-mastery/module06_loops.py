# Loops- for and while:

# Every program so far runs each line exactly once.
# But real problems constantly need repetition- checking every item in a list, retrying input until it's valid, processing transactions one by one. Doing this by copy-pasting the same line 100 times would be insane.
# Loops let you say "do this repeatedly" instead.

# while- repeat as long as a condition stays true

count = 1

while count <= 5:
    print(count)
    count += 1

# The single most dangerous mistake with while- the infinite loop:

# count = 1
# while count <= 5:
#     print(count)

# for- repeat a specific, known number of times (or over a known collection)

for i in range(5):
    print(i)
# Sequence will always starts from 0, going up to (but not inlcuding the last number or in this case you can see the number is 5).

for i in range(1, 6):
    print(i)
# This version explicitly starts at 1 and stops before 6, giving us 1,2,3,4,5- often clearer when you want to start from 1 instead of 0.

# for vs while-
# When to use for when you know (or can calculate) exactly how many times you need to repeat, or when you're going through a known collection of things.
# Use while when you're repeating until some condition becomes true or false, and you don't know in advance exactly how many repetitions that'll take- like retrying user input until it's valid.

# break and continue- controlling a loop from inside

for i in range(10):
    if i == 5:
        break
    print(i)

# break immediately exits the loop entirely, no matter how many repetitions were left. This prints 0,1,2,3,4 then stops completely- 5 through 9 never happen.

for i in range(5):
    if i == 2:
        continue
    print(i)

# continue skips just the current repetition and moves to the next one- the loop keeps going otherwise. This prints 0,1,3,4- 2 gets skipped, but 3 and 4 still run afterward.

# The genuinely useful real pattern- validating input with while

while True:
    age_input = input("Enter your age: ")
    try:
        age = int(age_input)
        break
    except ValueError:
        print("Invalid input, please enter a whole number.")

print("Your age is:", age)

# while True: means "loop forever" — the only way out is the break inside the try, which only happens once a valid number is successfully entered. If the input is bad, except prints an error and the loop simply asks again, forever, until it gets something valid. This is a genuinely professional pattern — real programs use exactly this shape whenever they need guaranteed-valid input before moving forward.

