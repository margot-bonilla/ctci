"""
17.22 Word Transformer: Given two words of equal length that are in a dictionary,
write a method to transform one word into another word by changing only one letter at a time.
The new word you get in each step should eb in the dictionary

[NOT WORKING FINE]

"""
from shared.test import *
from collections import deque


class PathNode:
    def __init__(self, word, previous):
        self.word = word
        self.previous = previous


class BFSData:
    def __init__(self, root: str):
        self.to_visit = deque()
        self.visited = dict()

        source_path = PathNode(root, None)
        self.to_visit.append(source_path)
        self.visited[root] = source_path

    def is_finished(self):
        return len(self.to_visit) == 0


def get_wildcard_roots(word):
    words = []
    for i in range(len(word)):
        w = word[:i] + '_' + word[i + 1:]
        words.append(w)
    return words


def create_wildcard(words):
    wildcard = dict()
    for word in words:
        linked = get_wildcard_roots(word)
        for linked_word in linked:
            wildcard[linked_word] = word
    return wildcard


def get_valid_linked_words(word, wildcard_to_words):
    wildcards = get_wildcard_roots(word)
    linked_words = []
    for wild in wildcards:
        print(wild)
        words = wildcard_to_words[wild]
        for linked in words:
            if linked != word:
                linked_words.append(linked)

    return linked_words


def search_level(wildcard: dict, primary: BFSData, secondary: BFSData):
    """
    Search one level and return collision if any:
    """

    count = len(primary.to_visit)
    for i in range(count):
        path_node = primary.to_visit.popleft()
        word = path_node.word

        if word in secondary.visited:
            return word

        words = get_valid_linked_words(word, wildcard)
        for w in words:
            if w not in primary.visited:
                next_node = PathNode(w, path_node)
                primary.visited[w] = next_node
                primary.to_visit.append(next_node)


def merge_paths(bfs_1, bfs_2, connection):
    end_1 = bfs_1.visited[connection]
    end_2 = bfs_2.visited[connection]

    path_one = ''.join(end_1)
    path_two = ''.join(end_2)[::-1]
    path_two = path_two[1:]
    path_one += path_two

    return path_one


def transform(source, target, words):
    dictionary = create_wildcard(words)
    source_data = BFSData(source)
    target_data = BFSData(target)

    while not source_data.is_finished() and not target_data.is_finished():
        collision = search_level(dictionary, source_data, target_data)
        if collision:
            return merge_paths(source_data, target_data, collision)


if __name__ == "__main__":
    source = "DAMP"
    target = "LIKE"
    words = ["DAMP", "LIKE", "LAMP", "LIMP", "LIME"]
    check("LIKE", transform(source, target, words))
