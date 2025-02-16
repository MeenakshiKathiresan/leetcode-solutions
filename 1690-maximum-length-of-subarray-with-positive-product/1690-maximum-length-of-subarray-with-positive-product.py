class Solution:
    def getMaxLen(self, nums):
        pos, neg = 0, 0
        max_len = 0
        
        for num in nums:
            if num > 0:
                pos += 1
                neg = neg + 1 if neg > 0 else 0
            elif num < 0:
                new_pos = neg + 1 if neg > 0 else 0
                neg = pos + 1
                pos = new_pos
            else:
                pos, neg = 0, 0
            
            max_len = max(max_len, pos)
        
        return max_len
