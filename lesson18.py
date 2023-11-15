import random
import re

# Task 1

valid_emails = "abc-@mail.com"


class CheckMail:
    def __init__(self, mail):
        self.mail = self.validate(mail)

    @staticmethod
    def validate(mail: str) -> str:
        if bool(re.match(r'^[a-zA-Z0-9_.+-]+[^_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', mail)):
            return mail
        raise ValueError("Uncorrected mail")


# Task 2

class Boss:

    def __init__(self, name: str, company: str):
        self.id = random.randint(1, 999)
        self.name = name
        self.company = company
        self._workers = []

    def __repr__(self):
        return f"Boss are: {self.id}, {self.name}, {self.company}"

    @property
    def workers(self):
        text = f'Workers for {self.name} are:\n'
        for employ in self._workers:
            text += f'{employ["id"]}, {employ["name"]}\n'
        return text

    @workers.setter
    def workers(self, value: dict):
        self._workers.append(value)


class Worker:

    def __init__(self, name: str, boss: Boss):
        self.id = random.randint(1, 999)
        self.name = name
        self.boss = boss
        boss.workers = {"id": self.id, 'name': name}


# Task 3


class TypeDecorators:
    @staticmethod
    def to_int(func):
        def income(*args, **kwargs):
            return int(func(*args, **kwargs))
        return income

    @staticmethod
    def to_str(func):
        def income(*args, **kwargs):
            return str(func(*args, **kwargs))
        return income

    @staticmethod
    def to_bool(func):
        def income(*args, **kwargs):
            return bool(func(*args, **kwargs))
        return income
    @staticmethod
    def to_float(func):
        def income(*args, **kwargs):
            return int(func(*args, **kwargs))
        return income


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25

assert do_something('True') is True
