class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        if len(s) == 0: return 0
11        
12        ch_ind = {}
13        j = 0
14        max_s = 0
15        for i in range(len(s)):
16            if s[i] in ch_ind:
17                j = max(j, ch_ind[s[i]]+1)
18            ch_ind[s[i]] = i
19            max_s = max(max_s, i - j +1)
20        return max_s
        """

        if len(s) == 0: return 0
        ch_ind = {}
        left = 0
        res = 0

        for i in range(len(s)):
            if s[i] in ch_ind:
                left = max(left, ch_ind[s[i]] + 1)
            ch_ind[s[i]] = i
            res = max(i - left + 1, res)
        return res


