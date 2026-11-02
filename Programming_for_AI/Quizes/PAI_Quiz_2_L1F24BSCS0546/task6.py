def retry_on_failure(func, max_retries=3, fallback_value=[], *args, **kwargs):
    def wrapper():
        try:
            for i in range(3):
                result = func(*args, **kwargs)
        except ConnectionError:
            return "fallback"
    return wrapper


call_attempt = 0
@retry_on_failure(max_retries=3, fallback_value=[])
def fetch_remote_weights():
    global call_attempt
    call_attempt += 1
   
    if call_attempt < 3:
        raise ConnectionError("Server reset connection.")
    return [0.12, 0.45, 0.89]


fetch_remote_weights()