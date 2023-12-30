class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = {}
        for word in words:
            for ch in word:
                if ch not in counter:
                    counter[ch] = 0
                counter[ch] += 1
        
        for v in counter.values():
            if v % len(words) != 0:
                return False
        return True