from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)

        def backtrack():
            nonlocal res
            for char in count:
                if count[char] > 0:
                    res += 1
                    count[char] -= 1
                    backtrack()
                    count[char] += 1  
        
        res = 0
        backtrack()
        return res
