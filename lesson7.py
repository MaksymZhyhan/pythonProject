# Task1

def favorite_movie():
    movie = input("What is your favorite movie?: ")
    print("My favorite movie is named" " " + '{' + movie + '}')


favorite_movie()


# Task2

def make_country():
    country_name = input("Write a country: ")
    capital = (input("Write the capital of" " " + country_name + ":" " "))
    your_input = {country_name: capital}

    return your_input


dictionar = make_country()
print(dictionar)


# Task3

def make_operation():
    return choice


while True:
    print("Choose the operation: ")
    print("Addition - 1")
    print("Subtraction - 2")
    print("Multiplication - 3")
    print("Exit - 4")

    choice = input("Enter the number of operation: ")
    if choice == "4":
        print("GoodBye")
        break
    if choice not in "1 , 2, 3, 4":
        print("Wrong choice")
        continue
    a = float(input("Write a first number: "))
    b = float(input("Write a second number: "))
    c = float(input("Write a third number: "))

    if choice == "1":
        print("Result: ", a + b + c)
    elif choice == "2":
        print("Result: ", (a - b - c))
    elif choice == "3":
        print("Result: ", (a * b * c))
    break


make_operation()
