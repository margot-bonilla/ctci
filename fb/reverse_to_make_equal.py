import math

# Add any extra import statements you may need here


# Add any helper functions you may need here

"""
              a
A = [1, 2, 3, 4, 5, 6, 7]

        b
B = [1, 4, 3, 2, 5, 6, 7]
        k

"""


def are_they_equal(array_a, array_b):
    a = 0
    b = 0

    if len(array_a) != len(array_b):
        return False

    # first while
    while a < len(array_a) and array_a[a] == array_b[b]:
        a += 1
        b += 1

    k = b
    while k < len(array_b) and array_b[k] != array_a[a]:
        k += 1

    if k >= len(array_b):
        return False

    while k >= b:
        if array_b[k] != array_a[a]:
            return False
        k -= 1
        a += 1

    a += 1
    b = a

    while a < len(array_a) and b < len(array_b):
        if array_a[a] != array_b[b]:
            return False

    return True


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!
def printString(string):
    print('[\"', string, '\"]', sep='', end='')


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
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    n_1 = 4
    a_1 = [1, 2, 3, 4]
    b_1 = [1, 4, 3, 2]
    expected_1 = True
    output_1 = are_they_equal(a_1, b_1)
    check(expected_1, output_1)

    n_2 = 4
    a_2 = [1, 2, 3, 4]
    b_2 = [1, 2, 3, 5]
    expected_2 = False
    output_2 = are_they_equal(a_2, b_2)
    check(expected_2, output_2)

    # Add your own test cases here
