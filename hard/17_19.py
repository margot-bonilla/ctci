"""
17.19 Missing Two: You are given n array with all the numbers from 1 to N appearing exactly once,
except for one number that is missing. How can you find the missing number in O(N) time and O(1) space?
What if there were two numbers missing?

"""
import math
from shared.test import *


def second_degree(a, b, c):
    left = (-(b) - math.sqrt(b**2 - (4 * a * c))) // 2 * a
    right = (-(b) + math.sqrt(b**2 - (4 * a * c))) // 2 * a

    return int(left), int(right)



def mult(arr):
    result = 1
    for n in arr:
        result *= n
    return result


def missing_number(arr):
    n = len(arr) + 2
    sum_expected = (n * (n + 1)) // 2
    a_plus_b = sum_expected - sum(arr)

    mult_expected = math.factorial(n)
    a_per_b = mult_expected // mult(arr)

    return second_degree(-1, a_plus_b, -a_per_b)


if __name__ == "__main__":
    arr = [1, 3, 5]
    check((4, 2), missing_number(arr))

    arr = [1, 2, 3, 4, 6, 7, 8]
    check((9, 5), missing_number(arr))

    arr = [1, 2, 4, 5, 6, 8, 9]
    check((7, 3), missing_number(arr))

    arr = [3, 4, 5, 6, 7, 8]
    check((2, 1), missing_number(arr))
