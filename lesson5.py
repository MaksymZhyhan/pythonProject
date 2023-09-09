# Task 1
import random

first_list = []
n = 10
while True:
    for i in range(n):
        first_list.append(random.randint(1, 10))
    print(first_list)
    break
first_list.sort()
print(first_list[-1])


# Task 2

first_list = []
second_list = []
c = 10
while True:
    for i in range(c):
        first_list.append(random.randint(1, 10))
        second_list.append(random.randint(1, 10))
    print(first_list)
    print(second_list)
    break
print(set(first_list + second_list))


# Task 3

first_list = list(range(1, 101))
second_list = []
a = 0
while a < len(first_list):
    if first_list[a] % 7 == 0 and first_list[a] % 5 != 0:
        second_list.append(first_list[a])
    a += 1

print(second_list)
