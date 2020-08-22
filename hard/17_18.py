from collections import defaultdict


class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.is_final = False


class Trie:
    def __init__(self):
        self.root = TrieNode('*')

    def add(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode(w)
            node = node.children[w]
        node.is_final = True

    def find_strings_at_loc(self, word, start):
        strings = []
        index = start
        node = self.root
        while index < len(word):
            if word[index] not in node.children:
                break

            node = node.children[word[index]]
            if node.is_final:
                strings.append(word[start:index+1])
            index += 1
        return strings

    def searchAll(self, word):
        lookup = defaultdict(list)

        for i in range(len(word)):
            strings = self.find_strings_at_loc(word, i)
            for s in strings:
                lookup[s].append(i)
        return lookup


if __name__ == "__main__":
    T = ["ms", "si", "i"]
    b = "mississipi"
    trie = Trie()
    for t in T:
        trie.add(t)
    print(trie.searchAll(b))
