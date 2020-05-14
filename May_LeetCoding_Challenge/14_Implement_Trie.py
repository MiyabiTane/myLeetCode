class TreeNode:

    def __init__(self):
        self.word = False  # childrenがいなければTrue
        self.children = {}

class Trie:

    def __init__(self):
        
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        
        node = self.root
        for st in word:
            if not st in node.children:
                node.children[st] = TreeNode()
            node = node.children[st]
        node.word = True


    def search(self, word: str) -> bool:
        
        node = self.root
        for st in word:
            if not st in node.children:
                return False
            node = node.children[st]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        
        node = self.root
        for st in prefix:
            if not st in node.children:
                return False
            node = node.children[st]
        return True

trie = Trie()
trie.insert("apple")
trie.search("apple")
trie.search("app")
trie.startsWith("app")
trie.insert("app")
trie.search("app")



