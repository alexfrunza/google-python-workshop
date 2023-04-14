"""
    Evaluates an expression taken from keyboard. The expression can contain
    following operators (, ), +, -, *, /, ^.

    Example of usage:
    Input: (1 +2 / 3 *    (4 +     5 )     - 6 )
    Output:
    Sanitized expression is: ( 1 + 2 / 3 * ( 4 + 5 ) - 6 )
    Expression in postfix form is: 1 2 3 / 4 5 + * + 6 -
    The result of the expression is: 1

"""

import re
from operators import operators_expression_calculator as operators


class InvalidExpression(Exception):
    pass


def sanitize_expresssion(expression: str) -> str:
    """
    Transform expressions like this: "3    - 2 +    1 * 2"
    in: "3 - 2 + 1 * 2"
    :param expression:
    :return:
    """
    # re.split splits the expression and keeps the separators
    return " ".join(
        [element for element in re.split(r"(\W)", expression.replace(" ", ""))
         if element != ""])


def construct_postfix_expression(expression: str) -> str:
    """
    Transform an infix expression in a postfix expression
    :param expression:
    :return:
    """
    postfix_expression = []
    operators_stack = []

    expression = expression.split(" ")

    for element in expression:
        if element in list(operators):
            while len(operators_stack) > 0 and operators_stack[-1] != "(" and \
                    operators[element]["priority"] <= \
                    operators[operators_stack[-1]]["priority"]:
                postfix_expression.append(operators_stack.pop())

            operators_stack.append(element)
        elif element == "(":
            operators_stack.append(element)
        elif element == ")":
            while operators_stack[-1] != "(":
                postfix_expression.append(operators_stack.pop())

            # Remove "("
            operators_stack.pop()
        else:
            postfix_expression.append(element)

    while len(operators_stack) > 0:
        postfix_expression.append(operators_stack.pop())

    return " ".join(postfix_expression)


def evaluate_postfix_expression(expression: str) -> float:
    results_stack = []
    elements = expression.split(" ")

    for element in elements:
        if element in set(operators):
            if len(results_stack) < 2:
                raise InvalidExpression

            operand1 = results_stack.pop()
            operand2 = results_stack.pop()

            results_stack.append(
                operators[element]["function"](operand2, operand1))
        else:
            results_stack.append(float(element))

    if len(results_stack) != 1:
        raise InvalidExpression

    return results_stack[0]


def exit_prompt() -> bool:
    while True:
        response = input("Do you want to calculate something else? (y/n): ")

        if response == 'n':
            return True
        if response == 'y':
            return False


while True:
    try:
        expression = input("Enter an expression: ")
        expression = sanitize_expresssion(expression)

        if len(expression.split(" ")) in {1, 2}:
            raise InvalidExpression

        print("Sanitized expression is:", expression)

        expression = construct_postfix_expression(expression)
        print("Expression in postfix form is:", expression)
        print("The result of the expression is:",
              f"{evaluate_postfix_expression(expression):g}")

        exit_program = exit_prompt()
        if exit_program:
            print("Have a great day!")
            break

    except (InvalidExpression, ValueError):
        print("The expression is invalid, please try again. "
              f"Allowed operators are {', '.join(operators)}")
        continue
    except ZeroDivisionError:
        print("Zero division is not allowed!")
        continue
