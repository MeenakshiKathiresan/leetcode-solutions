from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        frequency = Counter(s)
        
        freq_set = set()
        
        deletions = 0
        
        for freq in frequency.values():
            while freq in freq_set:
                freq -= 1
                deletions += 1
            
            if freq > 0:
                freq_set.add(freq)
        
        return deletions
