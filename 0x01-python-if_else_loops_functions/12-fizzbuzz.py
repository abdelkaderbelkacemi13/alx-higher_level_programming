#!/usr/bin/python3
def fizzbuzz():
    for multi in range(1, 101):
        if multi % 3 == 0 and multi % 5 == 0:
            multi = "FizzBuzz"
        elif multi % 5 == 0:
            multi = "Buzz"
        elif multi % 3 == 0:
            multi = "Fizz"
        print(multi, end=" ")
