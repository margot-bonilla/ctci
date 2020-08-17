

def plus(a: int, b: int) -> int:
    carry = 0
    result = 0
    while a and b:
        if a & 1 == 1 and b & 1 == 1:
            result |= carry
            carry = 1
        elif a & 1 == 1 or b & 1 == 1:
            result |= (carry ^ 1)
        a >>= 1
        b >>= 1
        result <<= 1

    result |= a
    result |= b
    return result


def plusRecursive(a, b):
    if b == 0:
        return a
    # add without carrying
    summ = a ^ b

    # carry but don't add
    carry = (a & b) << 1

    return plusRecursive(summ, carry)

def plusIterative(a, b):
    while b:
        summ = a ^ b
        carry = (a & b) << 1
        a = summ
        b = carry
    return a


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
    check(3, plus(2, 1))
    check(3, plusIterative(2, 1))
    check(3, plusRecursive(2, 1))
    check(22, plus(15, 7))
    check(22, plusIterative(15, 7))
    check(22, plusRecursive(15, 7))
    check(8, plus(5, 3))
    check(8, plusIterative(5, 3))
    check(8, plusRecursive(5, 3))
