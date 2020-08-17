import math


# Add any extra import statements you may need here


# Add any helper functions you may need here


def matching_pairs(s, t):
    # I assume the lengh of both strings is the same

    matches = [False] * len(s)
    not_matching = set()

    match = 0
    for i in range(len(s)):
        if s[i] == t[i]:
            matches[i] = True  # TODO check if maybe I canr remove this array
            match += 1
        else:
            not_matching.add(s[i] + '' + t[i])

    if len(not_matching) == 0:
        return match - 2

    if len(not_matching) == 1:
        return match - 1

    for nm in not_matching:
        rev = nm[::-1]
        if rev in not_matching:
            return match + 2

    return match + 1


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
    s_1, t_1 = "abcde", "adcbe"
    expected_1 = 5
    output_1 = matching_pairs(s_1, t_1)
    check(expected_1, output_1)

    s_2, t_2 = "abcd", "abcd"
    expected_2 = 2
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

    # Add your own test cases here
