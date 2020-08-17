def missingBinary(arr, column):
    if column > len(arr):
        return 0

    one_bits = []
    zero_bits = []

    for t in arr:
        n = len(t) - 1
        if t[n - column] == 1:
            one_bits.append(t)
        else:
            zero_bits.append(t)

    if len(zero_bits) <= len(one_bits):
        v = missingBinary(zero_bits, column + 1)
        return (v << 1) | 0
    else:
        v = missingBinary(one_bits, column + 1)
        return (v << 1) | 1


def missing(arr):
    return missingBinary(arr, 0)


test_case_number = 1


def printString(string):
    print('[\"', string, '\"]', sep='', end='')


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
    arr = [
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 1, 0, 0],
    ]
    expexted = 2

    check(expexted, missing(arr))

