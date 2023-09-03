#Task1
import random
random_number = random.randint(1, 10)
print(random_number)
your_number = int(input("Guess the number between 1 - 10: "))
if int(your_number) == random_number:
    print("You are right")
else:
    print("Not your day! Try more!")



#Task2
name = input("What is your name? ")
age = input("How old are you? ")
print("Hello" ' ' + name, "on your next birthday you’ll be", int(age) + 1)



#Task3

some_word = input("Write some word: ")
random_word = random.sample(some_word, 5)
print(random_word)
my_string = "" .join(random_word)
random_string = [my_string for _ in range(5)]
all_string = " ".join(random_string)
print(all_string)
