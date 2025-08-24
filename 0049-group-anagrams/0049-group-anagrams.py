class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorted version can be key
        # freq map can be key

        freq = defaultdict(list)
        res = []
        for word in strs:
            freq["".join(sorted(word))].append(word)
        
        for val in freq.values():
            res.append(val)
            
        return res