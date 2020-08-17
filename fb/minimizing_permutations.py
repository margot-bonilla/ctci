import math


# Add any extra import statements you may need here

# Add any helper functions you may need here
class Node:
    def __init__(self, val, count):
        self.val = val
        self.count = count


def reverse(s, left, right):
    return s[:left] + s[left:right][::-1] + s[right:]


def minOperations(arr):
    size = len(arr)
    start = "".join([str(i) for i in arr])
    dest = "".join([str(i) for i in sorted(arr)])
    node = Node(start, 0)
    q = [node]
    visited = set()
    if start == dest:
        return 0

    while q:
        node = q.pop(0)
        if node.val in visited:
            continue

        original = node.val
        for i in range(2, size + 1):
            permutation = original
            for j in range(0, size - i + 1):
                permutation_2 = permutation
                permutation_2 = reverse(permutation_2, j, j + i)
                if permutation_2 == dest:
                    return node.count + 1

                q.append(Node(permutation_2, node.count + 1))

    return 0


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
    print('[', n, ']', sep='', end='')


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
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    n_1 = 5
    arr_1 = [1, 2, 5, 4, 3]
    expected_1 = 1
    output_1 = minOperations(arr_1)
    check(expected_1, output_1)

    n_2 = 3
    arr_2 = [3, 1, 2]
    expected_2 = 2
    output_2 = minOperations(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
