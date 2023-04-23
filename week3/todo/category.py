import csv
import os

from typing import List
from display import print_warning, print_board_string
from todo_exception import TodoException, TodoInterrupted


def validate_category_name(name: str, file_name: str):
    if "," in name:
        raise TodoException("The category can't contain commas!")
    if "#" in name:
        raise TodoException("The category can't contain the character '#'!")
    if name == "":
        raise TodoException("The category name can't be an empty string!")

    if category_exists(file_name, name):
        raise TodoException(f"Category {name} already exists!")


def add_category(file_name: str):
    name = input("Category name: ")
    name = name.strip()

    if name == 'q':
        raise TodoInterrupted

    validate_category_name(name, file_name)

    write_single_category_to_file(file_name, name)


def show_categories(file_name: str):
    categories = get_categories(file_name)

    if len(categories) == 0:
        print_warning("No categories available!")
        return

    print_board_string("Categories")
    for index, category in enumerate(categories, start=1):
        print(f'{index}. {category}')


def get_categories(file_name: str) -> List[str]:
    with open(file_name, "r") as categories_file:
        rows = csv.reader(categories_file, delimiter=",")
        for row in rows:
            return row

    # If no categories in file, return an empty list
    return []


def write_single_category_to_file(file_name: str, category: str):
    if os.stat(file_name).st_size == 0:
        with open(file_name, "w") as categories_file:
            categories_file.write(category)
    else:
        with open(file_name, "a") as categories_file:
            categories_file.write(f",{category}")


def category_exists(file_name: str, name: str) -> bool:
    categories = get_categories(file_name)

    return name in categories
