"""
Exercise 17.13 Re-Space


"""


def can_build(word, is_orig, dictionary):
    if word in dictionary and not is_orig:
        return True

    for i in range(len(word)):
        if word[:i] in dictionary and can_build(word[i:], False, dictionary):
            return True
    return False


def longest_word(worList):
    dictionary = set(worList)
    for word in sorted(worList, key=len, reverse=True):
        if can_build(word, True, dictionary):
            return word

    return ''


if __name__ == "__main__":
    dictionary = [
        "cat",
        "banana",
        "dog",
        "nana",
        "walk",
        "walker",
        "dogwalker",
        "dogwalkernan"
    ]
    print(f'longest word {longest_word(dictionary)}')

