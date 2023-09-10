# Task1
def some_words(sentence):

    a_dict = {}
    words = sentence.split()
    for word in words:
        word = word.strip(".,!?")
        word = word.lower()
        if word not in a_dict:
            a_dict[word] = 1
        else:
            a_dict[word] += 1
    return a_dict


some_sentence = input("Write some sentence: ")
result = some_words(some_sentence)
print(result)

# Task2

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
    }
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
    }
keys = list(stock.keys())
sum_values_stock = sum(stock[key] for key in keys)
print("Total stock:", sum_values_stock)
keys2 = list(prices.keys())
sum_values_price = sum(prices[key] for key in keys2)
print("Total price:", sum_values_price)

total_price = sum_values_stock * sum_values_price
print("Total price of the stock:", total_price)

# Task3

some_list = [(i, i**2) for i in range(1, 11)]
print(some_list)

# Task4

day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

number_of_the_week = {i + 1: day[i] for i in range(len(day))}
day_of_the_week = {day[i]: i + 1 for i in range(len(day))}

print(number_of_the_week)
print(day_of_the_week)
