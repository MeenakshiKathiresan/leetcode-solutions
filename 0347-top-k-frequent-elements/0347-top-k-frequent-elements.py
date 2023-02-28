class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        freq = {}
        
        for num in nums:
            freq[num] = freq.get(num, 0) +1
        
        for key, v in sorted(freq.items(), key=lambda item: item[1], reverse=True):
            if len(ans) < k:
                ans.append(key)
        return ans