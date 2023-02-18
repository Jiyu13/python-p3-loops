#!/usr/bin/env python3

def happy_new_year():
    # for i in range(10, 0, -1):
    #     print(i)
    i = 10
    while i > 0:
        print(i)
        i -= 1
    
    print("Happy New Year!")

def square_integers(int_list):
    # return [i ** 2 for i in int_list]
    squared = []
    for each in int_list:
        each = each ** 2
        squared.append(each)
    return squared


def fizzbuzz():
    for i in range(1, 101):
        # if i % 15 == 0:
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)
