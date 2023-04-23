import sys
import os.path

import display
import category
import task
from todo_exception import TodoException, TodoInterrupted

file_todos = ""
file_categories = ""

if len(sys.argv) == 1:
    file_todos = "todos"
    file_categories = "categories"
elif len(sys.argv) == 2:
    file_todos = sys.argv[1]
    file_categories = "categories"
else:
    file_todos = sys.argv[1]
    file_categories = sys.argv[2]


def create_file_if_not_exists(file_name: str):
    if not os.path.exists(file_name):
        with open(file_name, "x"):
            pass


create_file_if_not_exists(file_todos)
create_file_if_not_exists(file_categories)


def display_menu(sorting_method: tuple[str, bool]):
    display.print_board_string("TODO list app - main menu")
    print(f"""\
You need to type the name of the action you want to do.
If you type "q" from the main menu you will exit the application, otherwise
you will return to main menu.

Sorting method for showing tasks: {sorting_method[0]}, reverse {str(sorting_method[1]).lower()}

Options below are listed as "option name" - "action"

Options:
Add a new category - add_category
Show the list with categories - show_categories
Add a new task - add_task
Show tasks - show_tasks
Edit a task - edit_task
Delete a task - delete_task
Choose a sorting method for tasks - choose_sort
Filter the tasks - filter_tasks
Exit the application - q
""")


sorting_method = ("default", False)

while True:
    display_menu(sorting_method)

    try:
        action = input("Action: ")

        if action == "add_category":
            category.add_category(file_categories)
        elif action == "show_categories":
            category.show_categories(file_categories)
        elif action == "add_task":
            task.add_task(file_todos, file_categories)
        elif action == "show_tasks":
            task.show_tasks(file_todos,
                            sorting=sorting_method[0],
                            reverse=sorting_method[1])
        elif action == "edit_task":
            pass
        elif action == "delete_task":
            pass
        elif action == "choose_sort":
            sorting_method = task.choose_sort()
        elif action == "filter_tasks":
            task.filter_tasks(file_todos, sorting_method[0], sorting_method[1])
        elif action == 'q':
            break
        else:
            print("This action is not available!")
    except TodoException as e:
        print("ERROR:", e)
        continue
    except TodoInterrupted:
        continue
    else:
        print(f"Action {action} was done successfully!")
