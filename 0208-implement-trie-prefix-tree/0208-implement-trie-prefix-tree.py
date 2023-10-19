class Trie:

    def __init__(self):
        self.trie = {}
    def insert(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                new_node = {}
                node[char] = new_node
                node = new_node
            else:
                node = node[char]
        node['$'] = word

    def search(self, word: str) -> bool:
        node = self.trie
        for char in word:
            if char not in node:return False
            node = node[char]
        if '$' not in node:return False
        return True
    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for char in prefix:
            if char not in node:return False
            node = node[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)