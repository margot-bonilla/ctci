import math

# Add any extra import statements you may need here


# Add any helper functions you may need here
"""

 [12, 7, 6, 7, 6]
 sort

        l
 [6, 6, 7, 7, 12]
           r

 A = [6, 6, 7] sum = 19
 B = [12, 7]    sum = 19



"""


def balancedSplitExists(arr):
    arr.sort()
    left = 0
    right = len(arr) - 1

    A = []
    B = []
    sum_A = 0
    sum_B = 0

    while left < right:
        if sum_A == sum_B:
            A.append(arr[left])
            B.append(arr[right])
            left += 1
            right -= 1
            sum_A += A[-1]
            sum_B += B[-1]
        elif sum_A > sum_B:
            B.append(arr[right])
            right -= 1
            sum_B += B[-1]
        else:
            A.append(arr[left])
            left += 1
            sum_A += A[-1]

    return A[-1] < B[-1]


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
    arr_1 = [2, 1, 2, 5]
    expected_1 = True
    output_1 = balancedSplitExists(arr_1)
    check(expected_1, output_1)

    arr_2 = [3, 6, 3, 4, 4]
    expected_2 = False
    output_2 = balancedSplitExists(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
