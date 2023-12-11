# Task1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, course, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.course = course

    def study(self):
        print(f"{self.name} is studying at {self.course} course")


class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def teach(self):
        print(f"{self.name} is teaching and has salary in the amount of {self.salary}")


first_student = Student(3, "Jony", 23)
first_student.introduce()
first_student.study()

first_teacher = Teacher("Mr.Brown", 45, "245$")
first_teacher.introduce()
first_teacher.teach()


# Task2
class Mathematician:
    def square_nums(self, nums):
        return [num ** 2 for num in nums]

    def remove_positives(self, nums):
        return [num for num in nums if num < 0]

    def filter_leaps(self, years):
        def leap_year(year):
            if year % 4 == 0 and (year % 100 != 0 or year % 400 != 0):
                return True
            else:
                return False

        return [year for year in years if leap_year(year)]


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

print("All good")


# Task3

class Product:
    def __init__(self, type_, name, price):
        self.type = type_
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.income = 0
        self.products = {}
        self.premium = 30
        self.product_text = (
            "name: {}\n"
            "type: {}\n"
            "amount: {}\n"
            "price: {}\n"
            "premium: {}\n"
            "discount: {}\n"
        )

    def add(self, product: Product, amount):
        price = product.price
        product_premium = (price + 100) * self.premium
        p = {
            product.name: {
                "type": product.type,
                "amount": amount,
                "price": price + product_premium,
                "premium": product_premium,
                "discount": 0,
                "product": product
            }
        }
        self.products.update(p)

    def set_discount(self, identifier: str, percent: float, identifier_type="name"):
        def change_discount(val):
            val["discount"] = (val["price"] / 100) * percent

        if identifier_type in ["name", "type"]:
            for name, value in self.products.items():
                if identifier_type == "name" and name == identifier:
                    change_discount(value)
                    break
                elif identifier_type == "type" and value["type"] == identifier:
                    change_discount(value)
                    break

    def sell_product(self, product_name, amount):
        product = self.products.get(product_name)
        if product:
            if product["amount"] - amount >= 0:
                self.products[product_name]["amount"] -= amount
                self.premium += product["premium"] * amount
            else:
                raise ValueError(
                    f'There is no required quantity {amount}, in stock {product["amount"]}'
                )
        else:
            raise ValueError(
                f"This product store has`t product with name {product_name}"
            )

    def get_income(self):
        return self.income

    def get_all_products(self):
        products = self.products
        text = "Products:\n\n"
        for name, product in products.items():
            text += (
                    self.product_text.format(
                        name,
                        product["type"],
                        product["amount"],
                        product["price"],
                        product["premium"],
                        product["discount"],
                        "-" * 100,
                    )
                    + f'{"-" * 100}\n'
            )

        return text

    def get_product_info(self, product_name):
        product = self.products.get(product_name)
        if product:
            text = self.product_text.format(
                product_name,
                product["type"],
                product["amount"],
                product["price"],
                product["premium"],
                product["discount"],
            )
            return text


p = Product("Sport", "Football T-Shirt", 100)

p2 = Product("Food", "Ramen", 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell_product("Ramen", 10)

assert s.get_product_info("Ramen") == ("Ramen", 290)


# Task 4

class CustomException(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        if args:
            msg = args[0]
        self.log_error(msg)

    def log_error(self, msg):
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"Error: {msg}\n")


try:

    raise CustomException("This is a message")
except CustomException as e:
    print(f"Custom exception{e}")
