# Task1

def local_variables():
    b = 35
    c = "Fast"
    g = [2, 3, 6]
    variables = locals()
    count = len(variables)
    return count


print("All locals variables:", local_variables())


# Task2

def some_func(a):
    def inner_func(b):
        return a * b

    return inner_func


numbers1 = some_func(5)
numbers2 = some_func(7)
print(numbers2(5))


# Task3

def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums1 or nums2):
        return func1(nums1)
    else:
        return func2(nums2)


# Assertions

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]

assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]


