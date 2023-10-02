# Task1

def favorite_movie(movie):
    print(f"My favorite movie is named {movie}")


favorite_movie("The Lord of the Rings")


# Task2

def make_country(name, capital):
    country = {
        'name': name,
        'capital': capital
    }
    return country


country_dict = make_country('France', 'Paris')
print(country_dict)


# Task3

def make_operation(operator, *args):
    result = args[0] if args else 0

    if operator == '+':
        for num in args[1:]:
            result += num
    elif operator == '-':
        for num in args[1:]:
            result -= num
    elif operator == '*':
        for num in args[1:]:
            result *= num

    return result


print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))
