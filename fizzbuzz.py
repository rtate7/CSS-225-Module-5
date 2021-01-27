# Bob Tate
# 1/27/21
#
# Solution to Problem 2
# This program iterates through the integers from 1 to 50. For multiples
# of three, it prints "Divisible by three" instead of the number and for
# the multiples of five, it prints "Divisible by five" instead of the
# number. For numbers which are multiples of both three and five it prints
# divisible by both.

for number in range(1, 51):
    # all numbers divisible by both 3 and 5 are divisble by 15
    # and all numbers divisible by 15 are divisible by both 3 and 5
    if number % 15 == 0: 
        print("Divisible by both")
    elif number % 3 == 0:
        print("Divisible by three")
    elif number % 5 == 0:
        print("Divisible by five")
    else:
        print(number)