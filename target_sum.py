# Q1 target sum
"""Write a function that, when passed a list and a target sum, returns,
efficiently with respect to time used, two distinct zero-based indices
of any two of the numbers, whose sum is equal to the target sum.
If there are no such two numbers, the function should return None.
For the function call:

find_two_sum([3, 1, 5, 7, 5, 9], 10)

The function should return a single tuple containing any of the following pairs
of indices:

    (0, 3) (or (3, 0)) → 3 + 7 = 10
    (1, 5) (or (5, 1)) → 1 + 9 = 10
    (2, 4) (or (4, 2)) → 5 + 5 = 10
"""


def find_two_sum(lst, trgt):
    d = {}
    # for k, v in enumerate(lst):
    #     if v in d:
    #         pass
    #     else:
    #         d[v] = k

    for i, j in enumerate(lst):
        if trgt - j in d:
            return i, d[trgt - j]
        d[j] = i

    return None


print(
    find_two_sum(
        [
            3,
            4,
            6,
            3,
            6,
            2,
            9,
            0,
            12,
        ],
        12,
    )
)
