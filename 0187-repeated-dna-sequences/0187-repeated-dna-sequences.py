class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        keys = set()
        res = set()
        for i in range(9, len(s), 1):
            curr = s[i - 9: i + 1]
            if curr in keys:
                res.add(curr)
            else:
                keys.add(curr)
        return list(res)

            