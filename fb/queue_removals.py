import math
# Add any extra import statements you may need here
from collections import deque


# Add any helper functions you may need here


def findPositions(arr, x):
    """
    just gonna follow the algorithm
    """
    # perform x iterations of the following
    output = []
    orig = deque()
    for idx, element in enumerate(arr):
        orig.append((idx + 1, element))

    q = deque()
    for _ in range(x):
        # 1. Pop x elements from the front of the queue
        max_element = -1
        for _ in range(min(x, len(orig))):
            original_idx, element = orig.popleft()
            if element > max_element:
                max_element = element

            q.append((original_idx, element))

        # 2. Find the one with the largest value and remove it
        # 3. For each one of the remaining elements that were popped
        while q:
            original_idx, last = q.popleft()
            if last == max_element:
                output.append(original_idx)
                # avoid duplicates
                max_element = -1
            else:
                orig.append((original_idx, max(last - 1, 0)))
    return output


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
    n_1 = 6
    x_1 = 5
    arr_1 = [1, 2, 2, 3, 4, 5]
    expected_1 = [5, 6, 4, 1, 2]
    output_1 = findPositions(arr_1, x_1)
    check(expected_1, output_1)

    n_2 = 13
    x_2 = 4
    arr_2 = [2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4]
    expected_2 = [2, 5, 10, 13]
    output_2 = findPositions(arr_2, x_2)
    check(expected_2, output_2)

    # Add your own test cases here
