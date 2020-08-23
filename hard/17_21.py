"""
17.21 Volume of Histogram: Imagine a histogram (bar graph). Design an algorithm to compute the volume of water
it could hold if someone pured water across the top. You can assume that each histogram bar has width 1.
"""
from shared.test import *


def water(arr):
    left = 0
    right = len(arr) - 1
    while left < len(arr) and arr[left] == 0:
        left += 1
    while right >= 0 and arr[right] == 0:
        right -= 1

    result = 0
    while left < right:
        if arr[left] <= arr[right]:
            accum = 0
            left_right = left + 1
            while (
                    left_right < right and
                    arr[left_right] <= arr[right] and
                    arr[left_right] <= arr[left]
            ):
                accum += arr[left_right]
                left_right += 1
            result += (left_right - (left + 1)) * arr[left] - accum
            left = left_right

        if arr[right] <= arr[left]:
            accum = 0
            right_left = right - 1
            while (
                    right_left > left and
                    arr[right_left] <= arr[left] and
                    arr[right_left] <= arr[right]
            ):
                accum += arr[right_left]
                right_left -= 1
            result += (right - (right_left + 1)) * arr[right] - accum
            right = right_left
    return result


if __name__ == "__main__":
    histogram = [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]
    expected = 26
    check(expected, water(histogram))

    histogram = [0, 0, 10, 0, 0, 9, 0, 0, 3, 0, 1, 0, 9, 0, 10, 0]
    expected = 88
    check(expected, water(histogram))

    histogram = [0, 0, 10, 0, 0, 9, 0, 0, 8, 0, 7, 0, 3, 0, 1, 0]
    expected = 45
    check(expected, water(histogram))

    histogram = [0, 0, 1, 0, 0, 3, 0, 0, 8, 0, 9, 0, 13, 0, 17, 0]
    expected = 38
    check(expected, water(histogram))

    histogram = [0, 0, 0, 0, 0]
    expected = 0
    check(expected, water(histogram))

    histogram = [0, 0, 1, 0, 0]
    expected = 0
    check(expected, water(histogram))

    histogram = [0, 1, 1, 0, 0]
    expected = 0
    check(expected, water(histogram))

    histogram = [1, 0, 0, 9, 0]
    expected = 2
    check(expected, water(histogram))
