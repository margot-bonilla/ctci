def countDigit(n, d):
    power_10 = 10**d
    next_power_10 = 10**(d + 1)

    right = n % power_10
    round_down = n - n % next_power_10
    round_up = round_down + next_power_10
    digit = (n // power_10) % 10

    if digit < 2:
        return round_down // 10
    elif digit == 2:
        return round_down // 10 + right + 1
    else:
        return round_up // 10


def nDigits(n):
    digits = 0
    while n > 0:
        n //= 10
        digits += 1
    return digits


def count2s(n):
    n2s = 0
    number_of_digits = nDigits(n)
    for i in range(number_of_digits):
        n2s += countDigit(n, i)
    return n2s


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
    check(9, count2s(25))
    check(41, count2s(200))
    check(1, count2s(2))
    check(160, count2s(300))
    check(169, count2s(325))
