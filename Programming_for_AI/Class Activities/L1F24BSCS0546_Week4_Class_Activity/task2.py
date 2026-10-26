from functools import reduce

def math_operation(operator, *numbers):

    if operator == "add":
        return sum(numbers)

    elif operator == "mul":
        return reduce(lambda x, y: x * y, numbers)

    else:
        return "Invalid, operator"

print(math_operation("mul", 2, 3, 4))