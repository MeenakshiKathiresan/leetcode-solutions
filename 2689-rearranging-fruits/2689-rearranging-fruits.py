
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        b1 = Counter(basket1)
        b2 = Counter(basket2)
        print(b1, b2)

        moves = []
        min_el = 999999999

        for k in b1.keys():
            min_el = min(k, min_el)
            if (b1[k] + b2[k]) % 2 != 0:
                return  -1

            if k in b2 and b1[k] > b2[k]:
                for i in range((b1[k] - b2[k])//2):
                    moves.append(k)
            elif k not in b2:
                for i in range(b1[k]//2):
                    moves.append(k)
            
        for k in b2.keys():
            min_el = min(k, min_el)
            if k in b1 and b2[k] > b1[k]:
                for i in range((b2[k] - b1[k])//2):
                    moves.append(k)
            elif k not in b1:
                for i in range(b2[k]//2):
                    moves.append(k)

        moves.sort()

        res = 0
        for i in range(len(moves)//2):        
            res += min(moves[i], 2 * min_el)
        return res
