# Task1
def oops():
    raise IndexError("This is IndexError")


def new_oops():
    try:
        oops()
    except IndexError as d:
        print(f"Caught an IndexError: {d}")


new_oops()


def oops2():
    raise KeyError("This is KeyError")


def new_oops2():
    try:
        oops()
    except IndexError as e:
        print(f"Caught an IndexError: {e}")


new_oops2()


# Task2

def calculate_func():
    try:
        a = float(input("Write first number: "))
        b = float(input("Write second number: "))
        result = (a ** 2) / b
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return result
    except ValueError:
        print("Please enter valid numerical values for a and b.")
        return None
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
result = calculate_func()
if result is not None:
    print(f"The result of (a^2) / b is: {result}")




