"""
    Operators implemented in calculator
"""


def add(a: float, b: float) -> float:
    return a + b


def sub(a: float, b: float) -> float:
    return a - b


def mul(a: float, b: float) -> float:
    return a * b


def div(a: float, b: float) -> float:
    return a / b


def power(a: float, b: float) -> float:
    return a ** b


operators = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "^": power,
}

# This dictionary consist operators which have a specific function and a
# priority. The priority is rated from 0 to inf, where 0 is the lowest priority
# and inf is the highest
operators_expression_calculator = {
    "+": {
        "function": add,
        "priority": 0,
    },
    "-": {
        "function": sub,
        "priority": 0,
    },
    "*": {
        "function": mul,
        "priority": 1,
    },
    "/": {
        "function": div,
        "priority": 1,
    },
    "^": {
        "function": power,
        "priority": 2,
    },
}
