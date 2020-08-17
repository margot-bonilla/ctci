import math

# Add any extra import statements you may need here


# Add any helper functions you may need here
"""

Brute Force:
[1.5] day 1 sum = 1.5

day = 1
counting = arr
while sum(counting) < 1000000:
  for i, g in enumerate(arr):
    counting[i] = g ** day


how can we improve? bin search?

the worst case we have g = 1 => max days we will need is 1.1 ~ 145 day
-> that means we can do the same process as before but instead from 1 to x days

changing the day to day /= 2 or day *= 2 up to the results


"""


def getBillionUsersDay(growthRates):
    billion = 1000000000
    left = 1
    right = billion
    counter = [0] * len(growthRates)
    middle = left + (right - left) // 2
    while left < right:
        middle = left + (right - left) // 2

        try:
            for i, g in enumerate(growthRates):
                counter[i] = g ** middle

            total = sum(counter)
            if total == billion:
                return middle
            elif total < billion:
                left = middle + 1
            else:
                right = middle - 1
        except:
            right = middle - 1

    return middle


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
    test_1 = [1.1, 1.2, 1.3]
    expected_1 = 79
    output_1 = getBillionUsersDay(test_1)
    check(expected_1, output_1)

    test_2 = [1.01, 1.02]
    expected_2 = 1047
    output_2 = getBillionUsersDay(test_2)
    check(expected_2, output_2)

    # Add your own test cases here
