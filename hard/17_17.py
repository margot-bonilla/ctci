"""
Exercise 17.13 Re-Space


"""
from shared.test import *


def maxMinutesUtil(appointments, index, memo):
    if index >= len(appointments):
        return 0

    if memo[index] == 0:
        with_next = appointments[index] + maxMinutesUtil(appointments, index + 2, memo)
        without_next = maxMinutesUtil(appointments, index + 1, memo)
        memo[index] = max(with_next, without_next)

    return memo[index]


def maxMinutes(appointments):
    memo = [0] * len(appointments)
    return maxMinutesUtil(appointments, 0, memo)


if __name__ == "__main__":
    appointments = [30, 15, 60, 75, 45, 15, 15, 45]
    check(180, maxMinutes(appointments))

