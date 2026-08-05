#Task 2: A Decorator that Takes an Argument

from functools import wraps

#Declare decorator
def type_converter(type_of_output):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator

#function 1
@type_converter(str)
def return_int():
    return 5

#function 2
@type_converter(int)
def return_string():
    return "not a number"

#Mainline code
if __name__ == "__main__":
    y=return_int()
    print(type(y).__name__ )

    try:
        y=return_string()
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer!")