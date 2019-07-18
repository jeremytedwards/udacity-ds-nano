# coding=utf-8

# from ipywidgets import widgets
# from IPython.display import display
# from ipywidgets import interact


# # Represents a single node in the Trie
# class TrieNode:
#     def __init__(self):
#         self.letter = '*'
#         self.children = []
#         self.terminal = True
#
#     def insert(self, char):
#         self.letter = char
#         self.children = TrieNode()
#         self.terminal = False


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        current = self.root

        for ltr in word:
            if ltr not in current:
                current[ltr] = {}
            current = current[ltr]

        current['*'] = True

    def find(self, prefix):
        current = self.root

        for ltr in prefix:
            if ltr not in current:
                return {}
            current = current[ltr]
        if '*' in current:
            return {}
        else:
            return current


class TrieNode:
    def __init__(self):
        self.letter = '*'
        self.children = []
        self.terminal = True

    def insert(self, char):
        self.letter = char
        self.children = TrieNode()
        self.terminal = False

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point

        for keys, values in self:
            yield keys



MyTrie = Trie()

wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefix_node = MyTrie.find(prefix)
        if prefix_node:
            print('\n'.join(prefix_node.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


f("an")
f("fu")
f("t")