#!/usr/bin/env python3
# Author ID: mvarghese10

# Purpose: To have a number of functions that return a selected number of items from a given list. Each function will return either a single item from the list OR will create a new list and return the entire new list.

# List

my_list = [100, 200, 300, 'six hundred']



# Definitions

def give_list():
    return my_list

def give_first_item():
    return str(my_list[0])

def give_first_and_last_item():
    return [my_list[0], my_list[-1]]

def give_second_and_third_item():
    return my_list[1:3]




# Main block

if __name__ == '__main__':
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())


