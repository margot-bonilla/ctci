def validate(arr, candidate):
    count = 0
    for n in arr:
        if n == candidate:
            count += 1

    return count > len(arr)/2


def get_candidate(arr):
    majority = 0
    count = 0
    for n in arr:
        if count == 0:
            majority = n
        if majority == n:
            count += 1
        else:
            count -= 1

    return majority


def get_majority(arr):
    candidate = get_candidate(arr)
    return candidate if validate(arr, candidate) else -1



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
    arr = [3, 2, 3, 4, 3, 3, 3, 3, 1, 2, 3, 4, 2]
    check(3, get_majority(arr))

    arr = [1, 2, 3, 4, 5]
    check(-1, get_majority(arr))

    arr = [5, 1, 5, 1, 5, 1, 5, 1, 5]
    check(5, get_majority(arr))

    arr = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]
    check(-1, get_majority(arr))
