"""
17.18 Shortest Subsequence: You are given two arrays, one shorter (with all distinct elements) and one
longer. Find the shortest subarray in the longer array that contains all the elements in the shorter
array. The items can appear in any order

example:
Input:  [1, 5, 9]
        [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
"""
from collections import defaultdict

class Window:
    def __init__(self, minlen):
        self.minlen = minlen
        self.left = 0
        self.right = 0


def shortest_subsequence(short, long):
    # as they are distinct I won't save a dict, just a set to keep track
    target = set(short)
    visited = defaultdict(int)
    left = 0
    right = 0
    window = Window(len(long))
    while right < len(long):
        while right < len(long) and target > visited.keys():
            if long[right] in target:
                visited[long[right]] += 1
            right += 1
        while left < right and target == visited.keys():
            if right - left < window.minlen:
                window.minlen = right - left
                window.left = left
                window.right = right
            visited[long[left]] -= 1
            if visited[long[left]] <= 0:
                del visited[long[left]]

            left += 1

    return [window.left, window.right - 1]


if __name__ == "__main__":
    short = [1, 5, 9]
    longer = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
    print(shortest_subsequence(short, longer))
