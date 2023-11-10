import os
from datetime import datetime
from functools import wraps


def log(filename):
    """Декоратор, который записывает результат вызова функции в лог-файл."""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            with open(os.path.join("..", "data", filename), "w", encoding="UTF=8") as file:
                date = datetime.now()
                try:
                    result = func(*args, **kwargs)
                    file.write(str(date) + " my_function ok")
                    return result
                except ZeroDivisionError:
                    file.write(f"{str(date)} {func.__name__} error:  {ZeroDivisionError} . Inputs:  {args}, {kwargs}")
                except TypeError:
                    file.write(f"{str(date)} {func.__name__} error:  {TypeError} . Inputs:  {args}, {kwargs}")

        return inner

    return wrapper


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(5, 2)
