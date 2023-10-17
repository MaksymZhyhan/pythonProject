# Task1

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I`m {self.age} years old")
        return self.firstname + self.lastname + str(self.age)


person1 = Person('Maks', 'Zhyhan', 27)
print(person1.talk())


# Task2

class Dog:
    age_factor = 7

    def __init__(self, age_dog):
        self.age_dog = age_dog

    def human_age(self):
        return self.age_dog + self.age_factor


equivalent = Dog(66)
print(equivalent.human_age())


# Task3

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0

    def first_channel(self):
        self.current_channel_index = 0
        return self.channels[self.current_channel_index]

    def last_channel(self):
        self.current_channel_index = len(self.channels) - 1
        return self.channels[self.current_channel_index]

    def turn_channel(self, channel_number):
        if channel_number <= len(self.channels) or channel_number > 0:
            self.current_channel_index = channel_number - 1
            return self.channels[self.current_channel_index]
        else:
            return "Invalid channel number"

    def next_channel(self):
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def previous_channel(self):
        self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def current_channel(self):
        return self.channels[self.current_channel_index]

    def is_exist(self, channel):
        if type(channel) == int:
            return "Yes" if 1 <= channel <= len(self.channels) else "No"
        elif type(channel) == str:
            return "Yes" if channel in self.channels else "No"
        else:
            return "Invalid type"


CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = TVController(CHANNELS)

assert controller.first_channel() == "BBC"

assert controller.last_channel() == "TV1000"

assert controller.turn_channel(1) == "BBC"

assert controller.next_channel() == "Discovery"

assert controller.previous_channel() == "BBC"

assert controller.current_channel() == "BBC"

assert controller.is_exist(4) == "No"

assert controller.is_exist("BBC") == "Yes"

