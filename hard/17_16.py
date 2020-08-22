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


def maxMinutesIterative(appointments):
    one_away = 0
    two_away = 0
    for i in range(len(appointments) - 1, -1, -1):
        current = max(two_away + appointments[i], one_away)
        two_away = one_away
        one_away = current
    return one_away



if __name__ == "__main__":
    appointments = [30, 15, 60, 75, 45, 15, 15, 45]
    check(180, maxMinutes(appointments))
    appointments = [75, 105, 120, 75, 90, 135]
    check(330, maxMinutes(appointments))
    appointments = [30, 15, 60, 75, 45, 15, 15, 45]
    check(180, maxMinutesIterative(appointments))
    appointments = [75, 105, 120, 75, 90, 135]
    check(330, maxMinutesIterative(appointments))

