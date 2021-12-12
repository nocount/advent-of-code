# Advent 2019 Day 1 Puzzle 1
import math


def calculate_fuel(mass):
    return math.floor(mass/3) - 2


def calculate_fuel_fuel(fuel_mass):

    total_fuel = 0
    temp_fuel = fuel_mass
    while temp_fuel > 0:
        print(temp_fuel)
        total_fuel += temp_fuel
        temp_fuel = calculate_fuel(temp_fuel)

    return total_fuel


def calculate_fuel_inclusive(mass):

    total_fuel = 0
    temp_fuel = mass
    while 1:
        temp_fuel = calculate_fuel(temp_fuel)
        print(temp_fuel)
        if temp_fuel <= 0:
            break

        total_fuel += temp_fuel

    return total_fuel


if __name__ == '__main__':

    with open('input.txt', 'r') as input:
        fuel_sum = 0
        mass_sum = 0
        for line in input:
            fuel_sum += calculate_fuel_inclusive(int(line))
            mass_sum += int(line)

    print(mass_sum)
    print(fuel_sum)

    # fuel_sum = 100756
    # total_sum = calculate_fuel_inclusive(fuel_sum)
    # print(total_sum)
