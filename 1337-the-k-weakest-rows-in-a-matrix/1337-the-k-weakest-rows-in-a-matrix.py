class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = {}
        
        for i, row in enumerate(mat):
            res[i] = row.count(1)
        
        sorted_res = sorted(res.items(), key = lambda x: x[1])
        
        sorted_res = [val[0] for val in sorted_res ]
        
        return sorted_res[:k]