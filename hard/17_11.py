"""
Exercise 17.11 Word Distance
You have a large text file containing words. Given any two words, find the shortest distance
(in terms of number of words) between them in the file. If the operation will be repeated many
times for the same file (but different pairs of words), can you optimize your solution?

"""
import sys
from collections import defaultdict


def create_graph(text):
    graph = defaultdict(list)
    words = text.strip().split(" ")
    prev = words[0]
    for i in range(1, len(words)):
        word = words[i]
        graph[prev].append(word)
        graph[word].append(prev)
        prev = word
    return graph


def word_distance(text, w1, w2):
    """
    This is an example of a text to get the closest distance between one word and another for example MY_WORD
    can be repeated here (MY_WORD) and be compared with MY_OTHER_WORD, the response should be 4.
    """

    graph = create_graph(text)

    # traversal
    q = [w1]
    count = 0
    visited = set()
    while q:
        level = len(q)
        for _ in range(level):
            word = q.pop(0)
            if word in visited:
                continue
            visited.add(word)

            if w2 in graph[word]:
                return count
            q += graph[word]

        count += 1
    return count


def word_distance_optimized(text, w1, w2):
    # we create a has table to save the positions of the words w1 and w2:
    words = text.strip().split(" ")
    positions = defaultdict(list)
    for pos, word in enumerate(words):
        if word == w1:
            positions[w1].append(pos)
        if word == w2:
            positions[w2].append(pos)

    # return the shortest pair
    i = 0
    j = 0
    pos_w1 = positions[w1]
    pos_w2 = positions[w2]
    min_distance = sys.maxsize
    while i < len(pos_w1) and j < len(pos_w2):
        min_distance = min(min_distance, abs(pos_w1[i] - pos_w2[j]) - 1)
        if pos_w1[i] < pos_w2[j] and i < len(pos_w1) - 1:
            i += 1
        elif pos_w1[i] > pos_w2[j] and j < len(pos_w2) - 1:
            j += 1
        else:
            break

    return min_distance


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
    text = (
        """
        geeks for geeks contribute practice
        """
    )
    check(1, word_distance(text, 'geeks', 'practice'))

    text = (
        """
        this is an example of w1 why the words should w2 not be that close w1
        """
    )
    check(4, word_distance(text, 'w1', 'w2'))

    text = (
        """
        the quick the brown quick brown the frog
        """
    )
    check(2, word_distance_optimized(text, 'quick', 'frog'))

    text = (
        """
        geeks for geeks contribute practice
        """
    )
    check(1, word_distance_optimized(text, 'geeks', 'practice'))

    text = (
        """
        this is an example of w1 why the words should w2 not be that close w1
        """
    )
    check(4, word_distance_optimized(text, 'w1', 'w2'))
