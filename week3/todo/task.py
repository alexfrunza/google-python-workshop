import datetime
import csv
from typing import List

import category
from display import print_warning, print_board_string
from todo_exception import TodoException, TodoInterrupted


def validate_infos(infos: str):
    if infos == "":
        raise TodoException("The infos field from task can't be empty!")
    if "#" in infos:
        raise TodoException("The infos field can't contain the character '#'!")


def validate_date_limit(date: str):
    if date == "":
        raise TodoException("The date limit from task can't be empty!")

    date_format = "%d.%m.%Y %H:%M"
    try:
        datetime.datetime.strptime(date, date_format)
    except ValueError:
        raise TodoException("The date limit format is invalid or the date is "
                            "invalid! Use the format 'zz.mm.yyyy hh:mm'.")


def validate_assigned_to(name: str):
    if "#" in name:
        raise TodoException("The assigned to field can't contain the character '#'!")


def validate_category(file_categories: str, name: str):
    if name == "":
        raise TodoException("The category from task can't be empty!")
    if not category.category_exists(file_categories, name):
        raise TodoException("The category does not exist!")
    if "#" in name:
        raise TodoException("The category field can't contain the character '#'!")


def add_task(file_todos_name: str, file_categories_name: str):
    infos = input("Infos about the task: ")
    if infos == "q":
        raise TodoInterrupted
    validate_infos(infos)

    date_limit = input("Deadline (format zz.mm.yyyy hh:mm): ")
    if date_limit == "q":
        raise TodoInterrupted
    validate_date_limit(date_limit)

    assigned_to = input("Assigned to: ")
    if assigned_to == "q":
        raise TodoInterrupted
    validate_assigned_to(assigned_to)

    category_name = input("Category: ")
    if category == "q":
        raise TodoInterrupted
    validate_category(file_categories_name, category_name)

    task = [infos, date_limit, assigned_to, category_name]

    if task_exists(file_todos_name, infos):
        raise TodoException(f"A task with this description already exists!")

    with open(file_todos_name, "a") as file_todos:
        todos_writer = csv.writer(file_todos, delimiter="#")
        todos_writer.writerow(task)


def get_tasks(file_name: str) -> List[List[str]]:
    result = []
    with open(file_name, "r") as categories_file:
        rows = csv.reader(categories_file, delimiter="#")
        for row in rows:
            result.append(row)

    return result


def show_tasks(file_name: str):
    tasks = get_tasks(file_name)

    if len(tasks) == 0:
        print_warning("No tasks registered!")
        return

    print_board_string("Tasks")
    for index, task in enumerate(tasks, start=1):
        print(f'{index}. {" -- ".join(task)}')


def task_exists(file_name: str, task: str) -> bool:
    existing_tasks = get_tasks(file_name)

    return task in {description[0] for description in existing_tasks}
