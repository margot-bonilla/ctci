"""
17.20 Continuous Median: Numbers are randomly generated and passed to a method. Write a program to
 find and maintain the median value as new values are generated
"""
from heapq import heappush, heappop
from shared.test import *


def median(arr):
    left = []
    right = []
    output = []
    for n in arr:
        heappush(left, n)
        if len(left) > len(right):
            heappush(right, -heappop(left))
        if (
            len(left) > 0 and
            len(right) > 0 and
            left[0] < (-right[0])
        ):
            heappush(right, -heappop(left))
            heappush(left, -heappop(right))

        if len(left) == len(right):
            output.append((left[0] + (-right[0])) // 2)
        else:
            output.append(-right[0])

    return output


if __name__ == "__main__":
    arr = [8, 3, 1, 9, 7, 5, 4, 2, 1, 3]
    expected = [8, 5, 3, 5, 7, 6, 5, 4, 4, 3]
    check(expected, median(arr))

    arr = [7, 4, 1, 3, 7, 4, 2, 1]
    expected = [7, 5, 4, 3, 4, 4, 4, 3]
    check(expected, median(arr))
