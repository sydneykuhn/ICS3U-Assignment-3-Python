#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Sep 2020
# This program calculates the sum of two numbers
#    provided by user


def main():

    # this function calculates the sum

    # input
    number_of_classes_as_string = input("Enter number of classes held : ")
    classes_attended_as_string = input("Enter number of classes attended : ")

    # process
    number_of_classes = int(number_of_classes_as_string)
    classes_attended = int(classes_attended_as_string)

    attendance_rate = round((classes_attended / number_of_classes) * 100)
    print("\nYou have a {0}% attendance rate.".format(attendance_rate))

    if attendance_rate >= 75:
        print("Therefore you are eligible to take the class exam.")
    else:
        print("Therefore you are not eligible to take the class exam.")

    print("\nDone.")


if __name__ == "__main__":
    main()
