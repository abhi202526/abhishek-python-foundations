# 1. 17 // 5 and 17 % 5 — predict both, then verify.
a = 17
b = 5
print(a // b)
print(a % b)

# 2. Real scenario: you have ₹250, chocolates cost ₹40 each. Using // and %, calculate how many chocolates you can buy and how much money is left over. Print both clearly labeled.
a = 250
b = 40
print(a // b)
print(a % b)

# 3. Predict: print(5 == 5.0) — comparing an int and a float with the same value. True or False? Why, based on what you know about type conversion?
print(5 == 5.0)
print(type(5 == 5.0))
# Or
a = 5
b = 5.0
print(a == b)
# I think even though it is a float but after decimal the number is 0 so that's why python didn't even consider it.

# 4. Predict: does 10 % 2 == 0 correctly identify that 10 is even? Test it, then test it again with an odd number like 7.
a = 10
b = 2
print(a % b == 0)
a = 7
print(a % b == 0)

# 5. Short-circuit test — predict what this prints, and why it doesn't crash:
x = 0
print(x != 0 and (10 / x > 2))
# why: Because in why condition we need both the condition true and here first condition is false so that's why the final output will be false not true even though x = 0.

# 6. Combine everything: a person can vote if their age is 18 or above AND they are a citizen. Create two variables (age, is_citizen), write one line using and that prints whether they can vote, then test it with two different value combinations (change the variables and rerun) to confirm both True and False cases work.
age = 18
is_citizen = True
print(age >= 18 and is_citizen)
is_citizen = False 
print(age >= 18 and is_citizen)

# 7. Genuinely tricky — work it out by hand first, step by step, before running: what does 10 % 3 == 1 and 10 // 3 == 3 evaluate to overall? Show your hand-worked steps as a comment.
# Before running it: what does 10 % 3 == 1 and 10 // 3 == 3 ?
# 10 % 3 == 1 and it is true because if we divide 3 with 10 the remainder is 1 and 10 // 3 == 3 which is also a True, dividing 10 by 3 the quotient will be the 3.333333 but with // floor division it is 3.
 