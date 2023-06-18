#!/usr/bin/python3
def fizzbuzz():
    for add in range(1, 101):
        if add % 3 == 0 and add % 5 == 0:
            print("FizzBuzz ", end="")
        elif add % 3 == 0:
            print("Fizz ", end="")
        elif add % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(add), end="")
