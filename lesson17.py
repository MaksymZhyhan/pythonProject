import math


# Task 1

class Animal:

    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        return "Woof, Woof"


class Cat(Animal):
    def talk(self):
        return "Meow"


def generic_func(instance_class):
    if isinstance(instance_class, Animal):
        return instance_class.talk()


dog = Dog()
cat = Cat()

print("Dog say:", generic_func(dog))
print("Cat say:", generic_func(cat))


# Task 2


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday

    def __repr__(self):
        return f"Author ({self.name}, {self.country}, {self.birthday})"

    def __str__(self):
        return


class Book:
    

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        self.books = []
        all_existing_books = 0

    all_existing_books += 1


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author):
        all_books = Book(name, year, author)
        self.books.append(all_books)
        return all_books

    def group_by_author(self, author: Author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]


# Task 3


class Fraction:
    """Create object that includes arithmetic methods for fractions (+, -, /, *)"""

    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError(
                "Type of numerator, denominator of fraction must be integer!"
            )
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def reduction(numerator, denominator):
        """Return numerator, denominator after fractional reduction"""
        gcd = math.gcd(numerator, denominator)
        return int(numerator / gcd), int(denominator / gcd)

    def __add__(self, summand):
        if not isinstance(summand, Fraction) and not isinstance(summand, int):
            raise ValueError("Wrong type of second argument!")
        if isinstance(summand, int):
            summand = Fraction(summand, 1)

        denominator = math.lcm(self.denominator, summand.denominator)
        numerator = int(
            (self.numerator * denominator / self.denominator)
            + (summand.numerator * denominator / summand.denominator)
        )
        numerator, denominator = Fraction.reduction(numerator, denominator)
        return Fraction(numerator, denominator)

    def __sub__(self, subtracted):
        if not isinstance(subtracted, Fraction) and not isinstance(subtracted, int):
            raise ValueError("Wrong type of second argument!")
        if isinstance(subtracted, int):
            subtracted = Fraction(subtracted, 1)

        denominator = math.lcm(self.denominator, subtracted.denominator)
        numerator = int(
            (self.numerator * denominator / self.denominator)
            - (subtracted.numerator * denominator / subtracted.denominator)
        )

        numerator, denominator = Fraction.reduction(numerator, denominator)
        return Fraction(numerator, denominator)

    def __mul__(self, multiplier):
        if not isinstance(multiplier, Fraction) and not isinstance(multiplier, int):
            raise ValueError("Wrong type of second argument!")
        if isinstance(multiplier, int):
            multiplier = Fraction(multiplier, 1)

        numerator = self.numerator * multiplier.numerator
        denominator = self.denominator * multiplier.denominator

        numerator, denominator = Fraction.reduction(numerator, denominator)
        return Fraction(numerator, denominator)

    def __truediv__(self, divisor):
        if not isinstance(divisor, Fraction) and not isinstance(divisor, int):
            raise ValueError("Wrong type of second argument!")
        if isinstance(divisor, int):
            divisor = Fraction(divisor, 1)

        numerator = self.numerator * divisor.denominator
        denominator = self.denominator * divisor.numerator

        numerator, denominator = Fraction.reduction(numerator, denominator)
        return Fraction(numerator, denominator)

    def __eq__(self, other):
        if not isinstance(other, Fraction) and not isinstance(other, int):
            raise ValueError("Wrong type of second argument!")
        if isinstance(other, int):
            other = Fraction(other, 1)
        numerator_1, denominator_1 = Fraction.reduction(
            self.numerator, self.denominator
        )
        numerator_2, denominator_2 = Fraction.reduction(
            other.numerator, other.denominator
        )
        return numerator_1 == numerator_2 and denominator_1 == denominator_2

    def is_bigger(self, other):
        """Return True if self fraction bigger then other"""
        denominator = math.lcm(self.denominator, other.denominator)
        numerator_1 = self.numerator * denominator / self.denominator
        numerator_2 = other.numerator * denominator / other.denominator
        return numerator_1 > numerator_2

    def __str__(self):
        return f"Fraction({self.numerator}, {self.denominator})"


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print("1/2 + 1/4 =", x + y)  # 1/2 + 1/4 == Fraction(3, 4)
    print("1/2 + 3 = ", x + 3)  # 1/2 + 3 == Fraction(7, 2)

    print("1/2 - 1/4 =", x - y)  # 1/2 - 1/4 == Fraction(1, 4)
    print("1/2 - 2 =", x - 2)  # 1/2 - 2 == Fraction(-3, 2)

    print("1/2 * 1/4 =", x * y)  # 1/2 * 1/4 == Fraction(1, 8)
    print("1/2 * 2 =", x * 3)  # 1/2 * 2 == Fraction(3, 2)

    print("1/4 / 1/2 =", y / x)  # 1/4 / 1/2 == Fraction(1, 2)
    print("1/2 / 3 =", x / 3)  # = Fraction(1, 6)

    print("Is 2/4 equal 1/2?: ", Fraction(2, 4) == Fraction(1, 2))  # True
    print("Is 4/2 equal 2?: ", Fraction(4, 2) == 2)  # True
    print("Is 2 equal 4/2?: ", 2 == Fraction(4, 2))  # True
    print("Is 3/2 equal 1/2?: ", Fraction(3, 2) == Fraction(1, 2))  # True

    print("Is 1/2 bigger then 1/4?: ", x.is_bigger(y))  # True
    print("Is 1/4 bigger then 1/2?: ", y.is_bigger(x))  # False
