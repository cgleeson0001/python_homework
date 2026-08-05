# Task 1: Writing and Testing a Decorator

import logging
from functools import wraps


logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler("./decorator.log", "a")
    logger.addHandler(file_handler)


def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        positional_parameters = list(args) if args else "none"
        keyword_parameters = kwargs if kwargs else "none"

        logger.info(
            f"function: {func.__name__}, "
            f"positional parameters: {positional_parameters}, "
            f"keyword parameters: {keyword_parameters}, "
            f"return: {result}"
        )

        return result

    return wrapper


# Function 1: no parameters and no return value
@logger_decorator
def say_hello():
    print("Hello, World!")


# Function 2: variable number of positional arguments
@logger_decorator
def positional_arguments(*args):
    print(f"Positional arguments received: {args}")
    return True


# Function 3: no positional parameters and variable keyword arguments
@logger_decorator
def keyword_arguments(**kwargs):
    print(f"Keyword arguments received: {kwargs}")
    return logger_decorator


# Mainline code
if __name__ == "__main__":
    say_hello()
    positional_arguments("Python", 3, True)
    keyword_arguments(
        name="Chantel",
        assignment=3,
        topic="decorators",
    )