import math


# Add any extra import statements you may need here


# Add any helper functions you may need here


def rotationalCipher(input, rotation_factor):
    # Write your code here
    result = ''
    for s in input:
        c = ord(s)
        if ord('a') <= c <= ord('z'):
            c += rotation_factor % 26
            if c > ord('z'):
                c = c % (ord('z') + 1) + ord('a')
            result += chr(c)

        elif ord('A') <= c <= ord('Z'):
            c += rotation_factor % 26
            if c > ord('Z'):
                c = c % (ord('Z') + 1) + ord('A')
            result += chr(c)

        elif ord('0') <= c <= ord('9'):
            c += rotation_factor % 10
            if c > ord('9'):
                c = c % (ord('9') + 1) + ord('0')
            result += chr(c)
        else:
            result += chr(c)

    print(input)
    return result


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
    input_1 = "All-convoYs-9-be:Alert1."
    rotation_factor_1 = 4
    expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
    output_1 = rotationalCipher(input_1, rotation_factor_1)
    check(expected_1, output_1)

    input_2 = "abcdZXYzxy-999.@"
    rotation_factor_2 = 200
    expected_2 = "stuvRPQrpq-999.@"
    output_2 = rotationalCipher(input_2, rotation_factor_2)
    check(expected_2, output_2)

    # Add your own test cases here
