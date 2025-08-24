class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = {}
        final = []
        
        for str in strs:
            new_str = ''.join(sorted(str))
            if new_str not in ans:
                ans[new_str] = []
            ans[new_str].append(str)
        
        for k,v in ans.items():
            final.append(v)
        
        return final