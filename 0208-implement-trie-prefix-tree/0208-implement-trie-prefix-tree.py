class TrieNode:
    def __init__(self):
        self.alphabets = {}
        self.end = False
    
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        current = self.root
        
        for ch in word:
            if ch not in current.alphabets:
                current.alphabets[ch] = TrieNode()
            
            current = current.alphabets[ch]
        current.end = True
        
        
    def search(self, word: str) -> bool:
        current = self.root
        
        for ch in word:
            if ch not in current.alphabets:
                return False
            current = current.alphabets[ch]

        return current.end
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        
        for ch in prefix:
            if ch not in current.alphabets:
                return False
            current = current.alphabets[ch]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)