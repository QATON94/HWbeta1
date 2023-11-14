from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, который записывает результат вызова функции в лог-файл."""

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            now_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            try:
                result = func(*args, **kwargs)
                log_mess = f"{now_date} {func.__name__} ok\n"

            except Exception as err:
                log_mess = f"{now_date} {func.__name__} error: {type(err).__name__}. Inputs: {args}, {kwargs}\n"
                result = None
            if filename:
                with open(filename, "a") as file:
                    file.write(log_mess)

            else:
                print(log_mess)
            return result

        return inner

    return wrapper
