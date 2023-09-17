#Task1
import random
random_number = random.randint(1, 10)
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

def create_random_strings(some_word, rand_word):

    random_strings = []

    for _ in range(rand_word):
        random_string = ''.join(random.sample(some_word, len(some_word)))
        random_strings.append(random_string)

    return random_strings


some_word = input("Enter a word: ")
rand_word = 5

random_strings = create_random_strings(some_word, rand_word)

print("Generate random word")
for random_string in random_strings:
    print(random_string)
