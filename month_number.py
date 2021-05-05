#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Wed/May5/2021
# This program is a month program


def main():
    # this function checks what month name to desplay according to its number.

    # input
    month_number = int(input("Enter the number of a month(ex: 3 for March):"))

    # process & output
    if (month_number == 1):
        print("January")
    elif (month_number == 2):
        print("February")
    elif (month_number == 3):
        print("March")
    elif (month_number == 4):
        print("April")
    elif (month_number == 5):
        print("May")
    elif (month_number == 6):
        print("June")
    elif (month_number == 7):
        print("July")
    elif (month_number == 8):
        print("August")
    elif (month_number == 9):
        print("September")
    elif (month_number == 10):
        print("October")
    elif (month_number == 11):
        print("November")
    elif (month_number == 12):
        print("December")
    else:
        print("this number is not a month number!")

    print("\nDone.")


if __name__ == "__main__":
    main()
