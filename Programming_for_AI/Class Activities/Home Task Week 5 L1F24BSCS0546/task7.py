
def memoize_predictions(func):

   
    cache = {}

    def wrapper(*args, **kwargs):

        key = tuple(
            tuple(arg) if isinstance(arg, list) else arg
            for arg in args
        )

        
        if key in cache:

            print("[CACHE HIT] Returning cached inference result")

            return cache[key]

        result = func(*args, **kwargs)

        
        cache[key] = result

        print("[COMPUTE] Calculating fresh result")

        return result

    return wrapper


@memoize_predictions
def compute_feature_distance(vector_a, vector_b):

    return sum(
        (x - y) ** 2
        for x, y in zip(vector_a, vector_b)
    ) ** 0.5



result1 = compute_feature_distance(
    [1, 2, 3],
    [4, 5, 6]
)

print("First Result:", result1)


result2 = compute_feature_distance(
    [1, 2, 3],
    [4, 5, 6]
)

print("Second Result:", result2)
