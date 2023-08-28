# Task 1

day = 'sunshaine'
print(day[0]+ day[1] + day[7] + day[8])
print(len(day))

duck = ('fly " " ' )
print(duck[3])
print(len(duck))

print(day + day)

# Task 2

my_name = ('Maks')
my_name == my_name.lower()
question = (input(" What is your name? "))
if my_name.lower() == question:
    print(True)
else:
    my_name != question
    print(False)

# Task 3

print("Math quiz")
question = int(input("What will be the answer: (25+5)*2 ?"))
expression = 60
while True:
   if question == expression:
    print("You are a god")
   elif question != expression:
       print("Let`s try one more time!")
       break




# Task 4


number = (input("Write a mobile number: "))
if len(number) == 10 and number.isdigit():
    print("All good")
else:
    print("Your number is not correct!")