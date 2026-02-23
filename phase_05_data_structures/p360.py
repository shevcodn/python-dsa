class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end = True

    def find_words(self, board, words):
        for word in words:
            self.insert(word)
        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, self.root, "", result)
        return list(result)

    def dfs(self, board, i, j, node, path, result):
        if node.is_end:
            result.add(path)
            node.is_end = False

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in node.children:
            return

        char = board[i][j]
        board[i][j] = "#" 
        self.dfs(board, i + 1, j, node.children[char], path + char, result)
        self.dfs(board, i - 1, j, node.children[char], path + char, result)
        self.dfs(board, i, j + 1, node.children[char], path + char, result)
        self.dfs(board, i, j - 1, node.children[char], path + char, result)
        board[i][j] = char
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
trie = Trie()
print(trie.find_words(board, words))