from random import randrange


def swap(arr, a, b):
    aux = arr[a]
    arr[a] = arr[b]
    arr[b] = aux


def shuffleUtils(deck, n):
    if n == 0:
        return deck
    a = randrange(0, len(deck) - 1)
    b = randrange(0, len(deck) - 1)
    swap(deck, a, b)

    return shuffleUtils(deck, n - 1)


def shuffle(deck):
    return shuffleUtils(deck, randrange(0, 1000))


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
    deck = []
    for i in range(1, 53):
        deck.append(i)

    print(shuffle(deck))
