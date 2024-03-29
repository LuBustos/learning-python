"""Module providing a function printing python version."""

import sys
import os

# Get the absolute path of the folder containing the current script
current_dir = os.path.dirname(os.path.realpath(__file__))
# Get the absolute path of the 'utils' folder from the current folder
utils_dir = os.path.join(current_dir, '..', 'utils')
# Add the absolute path of 'utils' to the module search path
sys.path.append(utils_dir)

import read_file  # pylint: disable=import-error,

def main():
    """Main function"""
    data = read_file.read_file(
        "advent-of-code-2022/Day 3 - Rucksack Reorganization/input.txt")
    item_sum = prioritize_rearrangement(data)
    print("Part 1", item_sum)
    item_sum_part2 = prioritize_rearrangemenet_three_elves(data)
    print("Part 2", item_sum_part2)


def prioritize_rearrangement(lines: list[str]):
    """method"""
    total = 0
    for element in lines:
        element = element.strip()
        compartments = cut_rucksack(element)
        letter = search_same_letter(compartments[0], compartments[1])
        if letter == letter.upper():
            total += get_upper_letter_points(letter)
        else:
            total += get_lower_letter_points(letter)
    return total


def get_upper_letter_points(letter: str):
    """get upper letter point"""
    return ord(letter[0]) - 38


def get_lower_letter_points(letter: str):
    """get lower letter point"""
    return ord(letter[0]) - 96


def cut_rucksack(rucksack: str):
    """cut rucksack method"""
    cutted_rucksack = []
    middle_index = len(rucksack) // 2
    cutted_rucksack.append(rucksack[0:middle_index])
    cutted_rucksack.append(rucksack[middle_index:])
    return cutted_rucksack


def search_same_letter(first_half: str, rest: str):
    """Looking for the same letters"""
    for letter in first_half:
        if letter in rest:
            return letter
    return ""

# Part 2


def prioritize_rearrangemenet_three_elves(lines: list[str]):
    """Part 2"""
    total = 0
    group = 0
    compartments = []
    for element in lines:
        element = element.strip()
        compartments.append(element)
        if group == 2:
            letter = looking_long_array_and_search(
                compartments[0], compartments[1], compartments[2])
            if letter == letter.upper():
                total += get_upper_letter_points(letter)
            else:
                total += get_lower_letter_points(letter)
            group = 0
            compartments.clear()
        else:
            group += 1
    return total


def looking_long_array_and_search(first_c: str, second_c: str, third_c: str):
    """Looking long array method"""
    len_first = len(first_c)
    len_second = len(second_c)
    len_third = len(third_c)
    if len_first > len_second and len_first > len_third:
        return search_same_letter_in_three_compartments(first_c, second_c, third_c)

    if len_second > len_first and len_second > len_third:
        return search_same_letter_in_three_compartments(second_c, first_c, third_c)

    return search_same_letter_in_three_compartments(third_c, first_c, second_c)


def search_same_letter_in_three_compartments(main_c, second_c, third_c):
    """Search same letter method"""
    for letter in main_c:
        if letter in second_c and letter in third_c:
            return letter
    return ""


main()
