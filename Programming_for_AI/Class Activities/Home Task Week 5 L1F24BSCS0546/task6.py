
def retry_on_failure(max_retries=3, fallback_value=None):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for attempt in range(1, max_retries + 1):

                try:
                    print(f"Attempt {attempt}: Calling function...")

                    result = func(*args, **kwargs)

                    return result

                except (ConnectionError, TimeoutError) as error:

                    print(f"Attempt {attempt} failed: {error}")

            print("All retry attempts failed!")
            return fallback_value

        return wrapper

    return decorator


call_attempt = 0


@retry_on_failure(max_retries=3, fallback_value=[])
def fetch_remote_weights():

    global call_attempt

    call_attempt += 1

    if call_attempt < 3:
        raise ConnectionError("Server reset connection.")

    return [0.12, 0.45, 0.89]


result = fetch_remote_weights()

print("\nFinal Result:", result)
print("Total Calls:", call_attempt)
