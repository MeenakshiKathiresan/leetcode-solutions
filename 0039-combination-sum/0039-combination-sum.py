class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        n = len(candidates)
        def recurse(i, t, ls):
            if t == 0:
                res.append(ls.copy())
                return

            if i >= n:
                return
            
            if candidates[i] <= t:
                ls.append(candidates[i])
                recurse(i, t - candidates[i], ls)
                ls.pop()

            recurse(i + 1, t, ls)
        recurse(0, target, [])
        return res