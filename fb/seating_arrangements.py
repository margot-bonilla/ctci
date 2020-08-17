import math

# Add any extra import statements you may need here


# Add any helper functions you may need here
"""

[1 3 4 2 6 8 3]

max of any pair
minimum?

"""


def minOverallAwkwardness(arr):
    arr.sort()
    m = len(arr) // 2
    l = m - 1
    r = m + 1
    arrange = [0] * len(arr)
    idx = len(arr) - 1
    arrange[m] = arr[idx]
    idx -= 1
    while idx >= 0:
        if r < len(arr):
            arrange[r] = arr[idx]
            idx -= 1
            r += 1
        if l >= 0:
            arrange[l] = arr[idx]
            idx -= 1
            l -= 1

    max_height = 0
    size = len(arr)
    for i in range(size + 1):
        max_height = max(max_height, abs(arrange[i % size] - arrange[(i + 1) % size]))

    return max_height


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
    print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    arr_1 = [5, 10, 6, 8]
    expected_1 = 4
    output_1 = minOverallAwkwardness(arr_1)
    check(expected_1, output_1)

    arr_2 = [1, 2, 5, 3, 7]
    expected_2 = 4
    output_2 = minOverallAwkwardness(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
