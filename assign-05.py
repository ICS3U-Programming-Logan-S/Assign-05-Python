#!/usr/bin/env python3
# Created by: Logan Sweeney
# Created on: Dec. 2, 2021
# Area of a Trapezoid
# This program will ask the user for the dimensions of a trapezoid.
# It will then calculate the area and perimeter then display it to the user.
import math
import time
import sys


def main():

    print("Hello! Today, we will calculate the area "
          + "and perimeter of a Trapezoid.")
    side_a = int(input("Enter side a (cm): "))
    side_b = int(input("Enter side b (cm): "))
    side_c = int(input("Enter side c (cm): "))
    side_d = int(input("Enter side d (cm): "))
    side_h = int(input("Enter side h (cm): "))
    area = (side_a + side_b) / 2 * side_h
    perimeter = (side_a + side_b + side_c + side_d)

    print("")
    print("The area of the trapezoid = {:.2f} cm^2. ".format(area))
    print("The perimeter of the trapezoid = {:.2f} cm. ".format(perimeter))


if __name__ == "__main__":
    main()
