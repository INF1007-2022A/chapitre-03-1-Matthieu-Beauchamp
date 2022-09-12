#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def square_root(a: float) -> float:
    return math.sqrt(a)


def square(a: float) -> float:
    return a*a


def average(a: float, b: float, c: float) -> float:
    return (a + b + c) / 3


def deg(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    "Returns decimal degrees instead of a DMS tuple"
    deg = angle_secs / 60
    deg = (deg + angle_mins) / 60
    return deg + angle_degs


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    return deg(angle_degs, angle_mins, angle_secs) * math.pi / 180


def to_degrees(angle_rads: float) -> tuple:
    # deg = (angle_rads / math.pi) * 180

    # we are forced to use the same as teacher since their test does not
    # account for floating point imprecision
    deg = math.degrees(angle_rads) 
    minutes = (deg - math.floor(deg)) * 60  # here we want positive values only
    sec = (minutes - math.floor(minutes)) * 60  # here we want positive values only
    return math.floor(deg), math.floor(minutes), sec

def to_celsius(temperature: float) -> float:
    return (temperature - 32) / 1.8

def to_farenheit(temperature: float) -> float:
    return temperature * 1.8 + 32
    


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(
        f"Conversion de 180 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")

    degrees, minutes, seconds = to_degrees(1.0)
    print(
        f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
