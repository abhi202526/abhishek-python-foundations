# a = "55.5"
# print(a)

# b = int(a)
# print(b)
# just testing that can int convert a float number along with quotes or a string them into integer and shows the result or error.

# Combined revision problem of all modules:

# Ask the user for an item's price (input()), and how many units they're buying (input()) — both need conversion (float for price, int for quantity), wrapped safely in try/except ValueError.
# Calculate the total cost (price * quantity).
# Ask the user if they have a discount coupon — accept "yes" or "no" as text (str, no conversion needed).
# If they said "yes", apply a 10% discount (total - total * 0.1) — otherwise, keep the total unchanged. (Use an if/else — you've used this pattern before, even before we formally cover Module 5's full depth.)
# Using // and %, calculate how many ₹50 notes it would take to pay this total, and how much change (in rupees) would be left over — remember floor division and modulo work together for exactly this kind of "how many whole X fit" problem.
# Print a clean, fully labeled summary at the end — item cost, quantity, total, whether a discount was applied, final amount, notes needed, and change — using f-strings throughout, not comma-separated print().
# Deliberately test it three times: once with completely valid input, once typing letters where a number is expected (confirm your except catches it), and once entering 0 for quantity (this won't crash — but think about what the output should logically show, and confirm it actually shows that).

# # Piece 1- Get price and quantity, safely:
# price_input = input("Enter item price: ")
# quantity_input = input("Enter quantity: ")

# try:
#     price = float(price_input)
#     quantity = int(quantity_input)
#     # ... rest goes here, still inside try
# except ValueError:
#     print("Please enter valid numbers.")

# # Piece 2- Calculate total:
# total = price * quantity

# # Piece 3- Ask about the coupon:
# coupon = input("Do you have a discount coupon? (yes/no): ")

# # Piece 4- Apply discount conditionally:
# if coupon == "yes":
#     total = total - total * 0.1

# # Piece 5- Notes and change:
# notes_needed = total // 50
# change = total % 50

# # Piece 6- Print the summary:
# print(f"Total cost: {total}")
# # ...continue for the rest

# Final code:
price_input = input("Enter item prices: ")
quantity_input = input("Enter quantity: ")

try:
    price = float(price_input)
    quantity = int(quantity_input)

    total = price * quantity

    coupon = input("Do you have a discount coupon? (yes/no): ")

    if coupon == "yes":
        total = total - total * 0.1

    notes_needed = total // 50
    change = total % 50

    print(f"Item price: {price}")
    print(f"Quantity: {quantity}")
    print(f"Total cost: {total}")
    print(f"Notes needed: {notes_needed}")
    print(f"Change: {change}")

except ValueError:
    print("Please enter valid numbers.")