import math

# Add any extra import statements you may need here


# Add any helper functions you may need here


"""
students:
unique integers from  1 to N -> not sorted
student i signs yearbook (holding)


Initially -> each student holds their own yearbook

each minute:
 step 1: student i signs yearbook holding
 step 2: pass yearbook to student arr[i] (arr[i] can be i)

once the student has their own book again should stop participating

return array with number of signatures

n in range [n, 100000]
each value arr[i] is in the range [1, n] and distinct


example:
current      [3, 4, 1, 6, 5, 7, 2]
signatures   [2, 4, 3, 3, 1, 3, 3]
              1  2  3  4  5  6  7

"""


def findSignatureCounts(arr):
    signatures = [1] * len(arr)
    for i in range(len(arr)):
        next_pos = arr[i] - 1
        while next_pos != i:
            signatures[i] += 1
            next_pos = arr[next_pos] - 1

    return signatures


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
    arr_1 = [2, 1]
    expected_1 = [2, 2]
    output_1 = findSignatureCounts(arr_1)
    check(expected_1, output_1)

    arr_2 = [1, 2]
    expected_2 = [1, 1]
    output_2 = findSignatureCounts(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
