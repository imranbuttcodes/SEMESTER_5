def wrapper(func):
    def smart_wrapper(*args, **kwargs):

        print("Logging: Function call initiated.")
        result = func(*args, **kwargs)


        return result
    
    return smart_wrapper


@wrapper
def base_calculator(a, b, operation="sum"):

    if operation == "mul":
        return a * b
    elif operation == "sum":
        return a + b

    return "Invalid operator entered!"



print("Result: ",base_calculator(2,3))
