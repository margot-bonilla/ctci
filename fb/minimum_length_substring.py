import math
# Add any extra import statements you may need here
from collections import defaultdict
import sys

# Add any helper functions you may need here


"""

order does matther!

min length?

example

s = d c c c b e f e c e  
t = c e f

              l
d c c c b e f e c e  
                    r

desirable {
 c: 1
 e: 1
 f: 0
}
counter: {
  e: 2
  c: 1
}
"""


def is_included(a, b):
    """
      compare if dictionary a is equal (keys) and same or bigger values
    """
    if len(a) != len(b):
        return False

    for key, value in a.items():
        if key not in b or a[key] < b[key]:
            return False
    return True


def min_length_substring(s, t):
    counter = defaultdict(int)
    desirable = defaultdict(int)
    for c in t:
        desirable[c] += 1

    left = 0
    while left < len(s) and s[left] not in t:
        left += 1

    if left == len(s):
        return -1

    min_window = sys.maxsize
    right = left
    while right < len(s):
        while not is_included(counter, desirable) and right < len(s):
            if s[right] in desirable:
                counter[s[right]] += 1
            right += 1

        while is_included(counter, desirable) and left < right:
            if s[left] in desirable:
                min_window = min(right - left, min_window)
                counter[s[left]] -= 1
            left += 1

    if min_window == sys.maxsize:
        return -1

    return min_window


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
    s1 = "dcbefebce"
    t1 = "fd"
    expected_1 = 5
    output_1 = min_length_substring(s1, t1)
    check(expected_1, output_1)

    s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
    t2 = "cbccfafebccdccebdd"
    expected_2 = -1
    output_2 = min_length_substring(s2, t2)
    check(expected_2, output_2)

    # Add your own test cases here
    s3 = "dcccbefece"
    t3 = "cef"
    expected_3 = 3
    output_3 = min_length_substring(s3, t3)
    check(expected_3, output_3)

    s4 = "ADOBECODEBANC"
    t4 = "ABC"
    expected_4 = 4
    output_4 = min_length_substring(s4, t4)
    check(expected_4, output_4)


    """
      l
    A D O B E C O D E B A N C
    r
    ABC
   desirable {A: 1, B: 1, C: 1}
   counter: {A: 1, } 
    
    
    """


