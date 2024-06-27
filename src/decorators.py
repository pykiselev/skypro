import os
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, который логгирует результаты и ошибки в файл или консоль"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                # test = 1/0
                msg = f"{func.__name__} ok. Result: {result}"
                return result
            except Exception as err:
                msg = f"{func.__name__} error: {type(err).__name__}. Inputs: {args}, {kwargs}"
                raise err
            finally:
                if filename:
                    if not os.path.exists(r"log"):
                        os.mkdir(r"log")
                    with open(os.path.join(r"log", filename), "at") as file:
                        file.write(msg + "\n")
                else:
                    print(msg)

        return wrapper

    return decorator
