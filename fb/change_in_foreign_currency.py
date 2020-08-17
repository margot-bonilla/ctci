import math

# Add any extra import statements you may need here


# Add any helper functions you may need here


"""



denominations = [5, 10, 25, 100, 200]
targetMoney = 94

denominations = [4, 17, 29] 29 + 17 = 46 + 29 = 75
targetMoney = 75



let's branch possibilities

                      |-> - 4  = 67
      | -> -4 = 71 ---|-> - 17 = ... 
      |               |-> - 29
      |
75 -- | -> -17 = 53
      |
      | -> -29 = 46      


O(n^n)
we could improve the time Complexity with some cache -> O(n  * ?) <- that's important, let's check later

75 - 4 -17 is the same as 75 - 17 - 4 -> so we don't need to develop all this path


let's try first the recursion

def func(targetMoney, denomination):
  if targetMoney < 0:
    return False

  for d in denomination:
    if fun(targetMoney - d, denomination):
      return True

  return False


"""


def canGetExactChangeUtils(targetMoney, denominations, cache):
    if targetMoney == 0:
        cache[targetMoney] = True
        return True
    if targetMoney < 0:
        cache[targetMoney] = False
        return False

    if targetMoney in cache:
        return cache[targetMoney]

    for d in denominations:
        cache[targetMoney - d] = canGetExactChangeUtils(targetMoney - d, denominations, cache)
        if cache[targetMoney - d]:
            return True

    return False


def canGetExactChange(targetMoney, denominations):
    cache = {}
    response = canGetExactChangeUtils(targetMoney, denominations, cache)
    print(len(cache))
    return response


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
    target_1 = 94
    arr_1 = [5, 10, 25, 100, 200]
    expected_1 = False
    output_1 = canGetExactChange(target_1, arr_1)
    check(expected_1, output_1)

    target_2 = 75
    arr_2 = [4, 17, 29]
    expected_2 = True
    output_2 = canGetExactChange(target_2, arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
