# Practice Set- Module 6

# 1. Use a while loop to print numbers 1 through 10. Then, deliberately create an infinite loop(comment out the increment line), run it, watch it hang, and force-stop it with Ctrl+C in the terminal- paste what that looks like. Then fix it.

count = 1

while count <= 10:
    print(count)
    count += 1

# 2. Use a for loop with range() to print all even numbers from 1 to 20 (hint: think about how you'd check "is this number even"- you already know this from Module 3).

for i in range(1, 21):
    if (i % 2 == 0):
        print(i)

# 3. Build the real validated-input pattern above yourself: keep asking for a whole number until valid, using while True + try/except + break. Test it by typing letters first (should ask again), then a valid number (should stop and confirm).

while True:
    whole_num = input("Enter a whole number: ")
    try:
        wh_num = int(whole_num)
        break
    except ValueError:
        print("Error: Enter a valid input")

print("Valid whole number:", wh_num)

# 4. Combine for and if: loop through range(1, 51), and use continue to skip any numbeer divisible by 3, printing everything else. (Refresher: "divisible by 3" means number % 3 == 0.)

for i in range(1, 51):
    if (i % 3 == 0):
        continue
    print(i)

# 5. Genuinely tricky, combining loops with what you already know: write a program that keeps asking the user to enter chocolate prices one at a time, and stops when they type "done" (not a number). Keep a running total of all valid prices entered, and print the total once they're done. (Hint: you'll need while True, a way to check if the input is literally the text "done" before trying to convert it to a number, and a running-total variable that starts at 0 before the loop begins.)

total = 0

while True:
    price_input = input("Enter chocolate price (or type 'done' to finish): ")

    if price_input == "done":
        break

    try:
        price = float(price_input)
        total += price

    except ValueError:
        print("Error: Please enter a valid price or 'done'.")

print("Total price of chocolates:", total)