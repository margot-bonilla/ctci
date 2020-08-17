

def swapper(arr, a, b):
    arr[a] += arr[b]
    arr[b] = arr[a] - arr[b]
    arr[a] -= arr[b]

    return arr



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
    arr = [5, 3, 8, 2]
    check([5, 2, 8, 3], swapper(arr, 1, 3))

    arr = [8, 46, 2, 1, 0, -4, 6, 7, -2]
    check([8, -4, 2, 1, 0, 46, 6, 7, -2], swapper(arr, 1, 5))
