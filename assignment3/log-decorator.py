#Task 1: Writing and Testing a Decorator

#set up
import logging
from functools import wraps

logger = logging.getLogger(__name__+"_parameter_log")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler=logging.FileHandler("./decorator.log","a")
    logger.addHandler(file_handler)

def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result=func(*args, **kwargs)

        positional_parameters=list(args) if args else "none"
        keyword_parameters=kwargs if kwargs else "none"

        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(
            logging.INFO,
            f"positional parameters: {positional_parameters}"
        )
        logger.log(
            logging.INFO,
            f"keyword parameters: {keyword_parameters}"
        )
        logger.log(logging.INFO, f"return: {result}")

        return result
    return wrapper

#function 1
@logger_decorator
def say_hello():
    print("Hello, World!")


#function 2
@logger_decorator
def positional_arguments(*args):
    print(f"Positional arguments received: {args}")
    return True


#function 3
@logger_decorator
def keyword_arguments(**kwargs):
    print(f"Keyword arguments received: {kwargs}")
    return logger_decorator


#mainline_code
if __name__ == "__main__":
    say_hello()
    positional_arguments("Python", 3, True)
    keyword_arguments(name="Chantel", assignment=3, topic="decorators")