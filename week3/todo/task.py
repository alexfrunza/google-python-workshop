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
    if name == "":
        raise TodoException("The task needs a person to be assigned!")


def validate_category(file_categories: str, name: str):
    if name == "":
        raise TodoException("The category from task can't be empty!")
    if not category.category_exists(file_categories, name):
        raise TodoException("The category does not exist!")
    if "#" in name:
        raise TodoException("The category field can't contain the character '#'!")


def add_task(file_todos_name: str, file_categories_name: str):
    infos = input("Infos about the task: ")
    infos = infos.strip()

    if infos == "q":
        raise TodoInterrupted
    validate_infos(infos)

    date_limit = input("Deadline (format zz.mm.yyyy hh:mm): ")
    date_limit = date_limit.strip()

    if date_limit == "q":
        raise TodoInterrupted
    validate_date_limit(date_limit)

    assigned_to = input("Assigned to: ")
    assigned_to = assigned_to.strip()

    if assigned_to == "q":
        raise TodoInterrupted
    validate_assigned_to(assigned_to)

    category_name = input("Category: ")
    category_name = category_name.strip()

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


def show_tasks(file_name: str, sorting="default", reverse=False, filter_field=None, search=""):
    tasks = get_tasks(file_name)

    if len(tasks) == 0:
        print_warning("No tasks registered!")
        return

    if sorting != "default":
        fields = {
            "task": 0,
            "date": 1,
            "assigned_to": 2,
            "category": 3
        }

        if sorting == "date":
            date_format = "%d.%m.%Y %H:%M"
            tasks.sort(key=lambda task: datetime.datetime.strptime(task[1], date_format),
                       reverse=reverse)
        else:
            tasks.sort(key=lambda task: task[fields[sorting]], reverse=reverse)

    print_board_string("Tasks")
    for index, task in enumerate(tasks, start=1):
        if filter_field is None or search in task[filter_field]:
            print(f'{index}. {" -- ".join(task)}')


def task_exists(file_name: str, task: str) -> bool:
    existing_tasks = get_tasks(file_name)

    return task in {description[0] for description in existing_tasks}


def choose_sort() -> tuple[str, bool]:
    print("""\
Choose a number for wanted sorting method:
1. ascending by task name
2. descending by task name
3. ascending by date limit
4. descending by date limit
5. ascending by assigned person
6. descending by assigned person
7. ascending by category
8. descending by category
9. default
""")

    option = input("Your option: ")
    option = option.strip()

    if option == 'q':
        raise TodoInterrupted

    if option not in {str(element) for element in list(range(1, 10))}:
        raise TodoException("Your option is not on the list")

    sorting_field = "default"
    if option in {"1", "2"}:
        sorting_field = "task"
    elif option in {"3", "4"}:
        sorting_field = "date"
    elif option in {"5", "6"}:
        sorting_field = "assigned_to"
    elif option in {"7", "8"}:
        sorting_field = "category"

    return sorting_field, bool(int(option) % 2 - 1)


def filter_tasks(file_name: str, sorting: str, reverse: bool):
    print("""\
Enter the number corresponding to the field you want to search by:
1. Task
2. Expire time
3. Assigned to
4. Category
""")
    filter_field = input("Your option: ")
    filter_field = filter_field.strip()

    if filter_field == "q":
        raise TodoInterrupted

    if filter_field not in {"1", "2", "3", "4"}:
        raise TodoException("Your option is not on the list!")

    search = input("Enter what you want to search for: ")
    search = search.strip()

    if search == "q":
        raise TodoInterrupted

    if search == "":
        raise TodoException("The text you want to search by can't be empty!")

    show_tasks(file_name, sorting, reverse, int(filter_field) - 1, search)
