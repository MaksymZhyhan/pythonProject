# # Task1

def logger(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} called with {args}, {kwargs}')
        return func(*args, **kwargs)

    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


# Example usage
add(2, 5)
square_all(1, 2, 3, 4)


# Task2


def stop_words(words):
    def decorator(func):
        def wrapper(*args, **kwargs):
            name = func(*args, **kwargs)
            for word in words:
                name = name.replace(word, '*')
            return name

        return wrapper

    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

print("All good")


# Task3

def arg_rules(type_: str, max_length: int, contains: list):
    def decorator(func):
        def wrapper(name):
            if len(name) > max_length:
                return False
            if not isinstance(name, type_):
                return False
            for item in contains:
                if item not in name:
                    return False
            return func(name)

        return wrapper

    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

print("All good")
