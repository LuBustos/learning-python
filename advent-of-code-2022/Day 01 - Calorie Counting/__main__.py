"""Module providing a function printing python version."""


def read_file(path):
    """Reading txt files"""
    with open(file=path, mode="r", encoding='UTF-8') as file_handle:
        content = file_handle.readlines()
        return content


def main():
    """"Main function"""
    data = read_file("advent-of-code-2022/Day 01 - Calorie Counting/input.txt")
    # count calories - Part 1
    total_food_carried = calorie_count(data)
    total_food_carried.sort(reverse="true")
    elf_carrying_the_most_calories = total_food_carried[0]
    print(elf_carrying_the_most_calories)
    # Part 2
    first_max_food, second_max_food, third_max_food, *_ = total_food_carried
    three_elfes_carrying_the_most_calories = first_max_food + \
        second_max_food + third_max_food
    print(three_elfes_carrying_the_most_calories)


def calorie_count(lines: list[str]):
    """Count calorie function"""
    total_food_carrie_by_elves = []
    total_food = 0
    for element in lines:
        element = element.replace("\n", "").strip()
        if len(element) > 0:
            total_food += int(element)
        else:
            total_food_carrie_by_elves.append(total_food)
            total_food = 0
    return total_food_carrie_by_elves


main()
