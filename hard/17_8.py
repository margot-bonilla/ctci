from collections import defaultdict

def can_append(arr, value):
    if arr == None:
        return False
    if len(arr) == 0:
        return True

    h, w = arr[-1]
    v_h, v_w = value
    return h < v_h and w < v_w


def best_at_index(arr, solutions, index):
    value = arr[index]
    best_seq = []
    for i in range(index):
        solution = solutions[i] if i < len(solutions) else None
        if can_append(solution, value):
            best_seq = max(best_seq, solution)
    best = best_seq.copy()
    best.append(value)

    return best


def max_tower(arr):
    s = sorted(arr, key=lambda x: x[0])
    solutions = []
    best_seq = []
    for i in range(len(s)):
        longest_at_index = best_at_index(s, solutions, i)
        solutions.append(longest_at_index)
        best_seq = max(best_seq, longest_at_index)
    return best_seq


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
    people = [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]
    check(6, len(max_tower(people)))

    people = [(65, 100)]
    check(1, len(max_tower(people)))

    people = [(65, 100), (75, 150), (56, 90), (50, 190), (60, 95), (68, 100)]
    check(4, len(max_tower(people)))
