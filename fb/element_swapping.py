import math
# Add any extra import statements you may need here
import sys

# Add any helper functions you may need here
"""
k = 3
       0  1   2  3   4
arr = [8, 9, 11, 2, 1]

smallest (between 0 and k) = 8 idx=0


"""


def get_min(arr, left, right):
    min_value = sys.maxsize
    min_index = left
    for i in range(left, min(len(arr), right)):
        if arr[i] < min_value:
            min_value = arr[i]
            min_index = i

    return min_index


def findMinArray(arr, k):
    start = 0
    while k > 0:
        min_index = get_min(arr, start, k + 1)

        while min_index > 0:
            aux = arr[min_index]
            arr[min_index] = arr[min_index - 1]
            arr[min_index - 1] = aux
            min_index -= 1
            k -= 1

    return arr


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
    print('[', n, ']', sep='', end='')


def printIntegerList(array):
    size = len(array)
    print('[', end='')
    for i in range(size):
        if i != 0:
            print(', ', end='')
        print(array[i], end='')
    print(']', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    expected_size = len(expected)
    output_size = len(output)
    result = True
    if expected_size != output_size:
        result = False
    for i in range(min(expected_size, output_size)):
        result &= (output[i] == expected[i])
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printIntegerList(expected)
        print(' Your output: ', end='')
        printIntegerList(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    n_1 = 3
    arr_1 = [5, 3, 1]
    k_1 = 2
    expected_1 = [1, 5, 3]
    output_1 = findMinArray(arr_1, k_1)
    check(expected_1, output_1)

    n_2 = 5
    arr_2 = [8, 9, 11, 2, 1]
    k_2 = 3
    expected_2 = [2, 8, 9, 11, 1]
    output_2 = findMinArray(arr_2, k_2)
    check(expected_2, output_2)

    # Add your own test cases here
