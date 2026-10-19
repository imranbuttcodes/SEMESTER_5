#Write a decorator
import time

def validate_and_time(func):

    def wrapper(*args, **kwargs):
        if any(value < 0 for arg in args for value in arg):
            raise ValueError("Negative input parameters are not allowed.")

        start_time = time.perf_counter()
        function_result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time * 1000:.4f} ms")

        return function_result
    return wrapper

@validate_and_time
def compute_batch_loss(predictions, targets):
        if len(predictions) != len(targets):
            raise ValueError("Predictions and targets must have the same length.")

        loss = sum((p - t) ** 2 for p, t in zip(predictions, targets)) / len(predictions)
        return loss


print(compute_batch_loss([1.2, 2.5, 3.1], [1.0, 2.0, 3.0]))

try:
    compute_batch_loss([-1.0, 2.0], [1.0, 2.0])
except ValueError as e:
    print(f"Error: {e}")