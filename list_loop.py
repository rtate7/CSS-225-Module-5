# Bob Tate
# 1/27/21
#
# Solution to Problem 2
# This program iterates through a list of numbers twice.
# The first time through it prints all of the numbers.
# The second time through it prints each number and its square.

numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

print("Numbers:")
for number in numbers:
    print(str(number))

print("\nSquares:")
for number in numbers:
    print(str(number), "squared is:", str(number ** 2))

