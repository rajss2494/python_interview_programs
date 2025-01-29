"""Implement the function count_numbers that:

    Accepts a sorted list of unique integers.
    Efficiently (with respect to time complexity) counts the number of list
    elements that are less than the given parameter less_than.

    #Example
    count_numbers([1, 3, 5, 7], 4)
    Output : 2  # Because two elements (1, 3) are less than 4
"""


def count_element(lst, trgt):
    left, right = 0, len(lst)

    while left < right:
        mid = (left + right) // 2
        if trgt > lst[mid]:
            # count+=mid
            left = mid + 1
        elif trgt <= lst[mid]:
            right = mid
    return left


print(count_element([1, 3, 5, 7], 4))  # Output: 2
print(count_element([1, 2, 3, 4, 5, 6], 5))  # Output: 4
print(count_element([10, 20, 30, 40], 25))  # Output: 2
print(count_element([2, 4, 6, 8, 10], 1))  # Output: 0
print(count_element([2, 4, 6, 8, 10], 15))  # Output: 5
