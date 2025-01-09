from functools import wraps


def log(filename=""):
    """декоратор, который будет автоматически логировать начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки. Декоратор должен принимать
     необязательный аргумент filename, который определяет, куда будут записываться логи
     (в файл или в консоль)"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                result = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if not filename:
                    print(result)
                else:
                    with open(filename, "w") as file:
                        file.write(result)
                return result
            result = f"{func.__name__} {func(*args, **kwargs)}"
            if not filename:
                print(result)
            else:
                with open(filename, "w") as file:
                    file.write(result)
            return result

        return wrapper

    return decorator
