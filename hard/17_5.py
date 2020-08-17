def isLetter(x):
    return 'a' <= x <= 'z'


def longestSubarray(arr):
    n = len(arr)
    chart = [-2] * (2 * n + 1)
    chart[n] = -1

    count = 0
    maxlen = 0
    left = 0
    right = 0

    for i in range(n):
        count += -1 if isLetter(arr[i]) else 1
        if chart[count + n] >= -1:
            if maxlen < i - chart[count + n]:
                maxlen = i - chart[count + n]
                left = min(i, chart[count + n]) + 1
                right = max(i, chart[count + n])
        else:
            chart[count + n] = i

    return maxlen, left, right


def longestSubarray2(arr):
    indexes = { 0: -1 }
    count = 0
    maxlen = 0
    left = 0
    right = 0
    n = len(arr)
    for i in range(n):
        count += -1 if isLetter(arr[i]) else 1
        if count in indexes:
            if maxlen < i - indexes[count]:
                maxlen = i - indexes[count]
                left = indexes[count] + 1
                right = i
        else:
            indexes[count] = i

    return maxlen, left, right


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
    arr = ['a', '1', 'z', '4']
    expected = 4, 0, 3
    check(expected, longestSubarray(arr))

    arr_2 = ['1', '1', 'z', '4', '1', '1', '1', 'a', '2', 'a', '2']
    expected = 4, 6, 9
    check(expected, longestSubarray(arr_2))

    arr = ['a', '1', 'z', '4']
    expected = 4, 0, 3
    check(expected, longestSubarray2(arr))

    arr_2 = ['1', '1', 'z', '4', '1', '1', '1', 'a', '2', 'a', '2']
    expected = 4, 6, 9
    check(expected, longestSubarray2(arr_2))

