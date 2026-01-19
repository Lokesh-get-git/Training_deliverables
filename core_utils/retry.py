import time

def Retry(
        func,
        retries=3,
        delay=1,
        fallback=2,
        exceptions=(Exception,)
):
    current_delay=delay

    for attempts in range(1,retries+1):
        try:
            return func()
        except exceptions as e:
            if attempts==retries:
                raise
        time.sleep(current_delay)
        current_delay*=fallback
