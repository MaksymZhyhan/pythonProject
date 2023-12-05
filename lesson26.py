# Task1


def binary_search_recursive(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, high)
        else:
            return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return -1


sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_element = 5
result = binary_search_recursive(sorted_array, target_element, 0, len(sorted_array) - 1)

if result != -1:
    print(f"Element {target_element} found by index {result}.")
else:
    print(f"Element {target_element} is not found in the array.")


def fibonacci_search_recursive(arr, target, low, high):
    if low <= high:
        fib_m_minus_2 = 0
        fib_m_minus_1 = 1
        fib = fib_m_minus_1 + fib_m_minus_2

        while fib < (high - low + 1):
            fib_m_minus_2 = fib_m_minus_1
            fib_m_minus_1 = fib
            fib = fib_m_minus_1 + fib_m_minus_2

        mid = low + fib_m_minus_2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return fibonacci_search_recursive(arr, target, mid + 1, high)
        else:
            return fibonacci_search_recursive(arr, target, low, mid - 1)
    else:
        return -1


sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_element = 5
result = fibonacci_search_recursive(sorted_array, target_element, 0, len(sorted_array) - 1)

if result != -1:
    print(f"Element {target_element} found by index {result}.")
else:
    print(f"Element {target_element} is not found in the array.")
