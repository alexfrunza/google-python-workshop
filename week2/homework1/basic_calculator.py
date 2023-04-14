"""
    A basic calculator in cmd which ask for 2 operands and 1 operator, and then
    return the value of operand1 operator operand2.
"""

from operators import operators


# This exception is used to clear previous input if current input is 'C'
class ClearData(Exception):
    pass


def get_operand(name: str) -> float:
    while True:
        operand = input(f"Insert {name} operand: ")

        if operand == "C":
            raise ClearData

        try:
            operand = float(operand)
        except ValueError:
            print(f"The {name} operand must be a number")
            continue
        else:
            break

    return operand


def get_operator() -> str:
    while True:
        operator = input("Enter the operator: ")

        if operator == "C":
            raise ClearData

        if operator in operators:
            break

        print(f"The operator must be one of {', '.join(operators.keys())}")

    return operator


def exit_prompt() -> bool:
    while True:
        response = input("Do you want to calculate something else? (y/n): ")

        if response == 'n':
            return True
        if response == 'y':
            return False


while True:
    try:
        operand1 = get_operand("first")
        operator = get_operator()
        operand2 = get_operand("second")
    except ClearData:
        print("Data cleared...")
        continue

    if operator == '/' and operand2 == 0:
        print("The zero division is not allowed!")
        continue

    print(
        # 'g' format specifier remove insignificant trailing 0s
        f"The result of {operand1:g} {operator} {operand2:g} ="
        f" {operators[operator](operand1, operand2):g}")

    exit_program = exit_prompt()
    if exit_program:
        print("Have a great day!")
        break
