from collections import Counter
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        b1 = Counter(basket1)
        b2 = Counter(basket2)

        moves = []
        min_el = float('inf')

        for k in set(b1.keys()).union(b2.keys()):
            total = b1[k] + b2[k]
            if total % 2 != 0:
                return -1 

            min_el = min(min_el, k)
            diff = abs(b1[k] - b2[k])
            moves.extend([k] * (diff // 2)) 

        moves.sort()

        res = sum(min(x, 2 * min_el) for x in moves[:len(moves)//2])
        return res
