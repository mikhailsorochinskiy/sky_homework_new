def log(filename=""):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                result = f'{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}'
                if not filename:
                    print(result)
                else:
                    with open(filename, 'w') as file:
                        file.write(result)
                return result
            result = f'{func.__name__} {func(*args, **kwargs)}'
            if not filename:
                print(result)
            else:
                with open(filename, 'w') as file:
                    file.write(result)
            return result
        return wrapper
    return decorator

@log(filename="")
def get_mask_account(account_number: str) -> str:
    """Номер счета принимает вид: **XXXX (X - цифра)"""
    if len(account_number) != 20 or account_number.isdigit() is False:
        raise ValueError('Некорректное значение')
    return "**" + account_number[-4:]

print(get_mask_account('12345678'))