class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)

        res = []
        def recurse(i, t, ls):
            if t == 0:
                res.append(ls.copy())
                return

            for ind in range(i, n):
                if ind > i and candidates[ind] == candidates[ind-1]:
                    continue
                if candidates[ind] > t: 
                    break
                ls.append(candidates[ind])
                recurse(ind + 1, t - candidates[ind], ls)
                ls.pop()
            
        
        recurse(0, target, [])
        return res
                