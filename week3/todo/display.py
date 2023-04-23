def print_board_string(s: str):
    print("┏" + (len(s) + 2)*"━" + "┓")
    print("┃ " + s + " ┃")
    print("┗" + (len(s) + 2)*"━" + "┛")


def print_warning(s: str):
    print("WARNING:", s)
