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
    def __init__(self, numerator: int, denominator: int):
        if type(numerator) == int and type(denominator) == int:
            self.numerator = numerator
            self.denominator = denominator
        else:
            raise ValueError('Args must be integer')

    def __str__(self):
        print(f"{self.numerator}/{self.denominator}")
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        new_numerator, new_denominator = self.optimized(new_numerator, new_denominator)
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = other.numerator * self.denominator
        return new_numerator == new_denominator

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Ділення на нуль неможливе")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    @staticmethod
    def optimized(numerator, denominator):
        new_numerator = numerator
        new_denominator = denominator
        flag = True
        while flag:
            if not new_denominator % 2 and not new_numerator % 2:
                new_numerator = new_numerator / 2
                new_denominator = new_denominator / 2
            else:
                flag = False
        return int(new_numerator), int(new_denominator)


x = Fraction(1, 2)
y = Fraction(1, 4)
print(x + y)
print(Fraction(3, 4))
assert x + y == Fraction(3, 4)
