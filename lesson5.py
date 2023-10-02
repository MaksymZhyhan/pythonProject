# Task 1
import random

first_list = []
n = 10
i = 0
while i < n:
    for i in range(n):
        first_list.append(random.randint(1, 100))
    i += 1
    print(first_list)
    break
first_list.sort()
print("Largest number", first_list[-1])

# Task 2

first_list = []
i = 0
while i < 10:
    num = random.randint(1, 10)
    first_list.append(num)
    i += 1

second_list = []
i = 0
while i < 10:
    num = random.randint(1, 10)
    second_list.append(num)
    i += 1

third_list = list(set(first_list) & set(second_list))

print("First list", first_list)
print("Second list", second_list)
print("Third list", third_list)

# Task 3

first_list = list(range(1, 101))
second_list = []
a = 0
while a < len(first_list):
    if first_list[a] % 7 == 0 and first_list[a] % 5 != 0:
        second_list.append(first_list[a])
    a += 1

print(second_list)
