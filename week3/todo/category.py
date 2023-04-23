import csv
import os

from typing import List
from display import print_warning, print_board_string
from todo_exception import TodoException, TodoInterrupted


def add_category(file_categories: str):
    name = input("Category name: ")

    if name == 'q':
        raise TodoInterrupted

    if "," in name:
        raise TodoException("The category can't contain commas!")

    categories = get_categories(file_categories)

    if name in categories:
        raise TodoException(f"Category {name} already exists!")

    write_single_category_to_file(file_categories, name)


def show_categories(file_categories: str):
    categories = get_categories(file_categories)

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
