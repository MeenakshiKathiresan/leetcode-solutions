class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for fruit in fruits:
            for i, b in enumerate(baskets):
                if fruit <= b:
                    baskets[i] = 0
                    break
        
        res = 0
        print(baskets)
        for b in baskets:
            if b != 0:
                res += 1
        return res