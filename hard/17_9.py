def kth_number(k):
    x = 1
    q3 = []
    q5 = []
    q7 = []
    for _ in range(1, k):
        q3.append(x*3)
        q5.append(x*5)
        q7.append(x*7)

        x = min(q3[0], q5[0], q7[0])
        if x == q3[0]:
            q3.pop(0)
        if x == q5[0]:
            q5.pop(0)
        if x == q7[0]:
            q7.pop(0)

    return x


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
    check(1, kth_number(1))
    check(9, kth_number(5))
