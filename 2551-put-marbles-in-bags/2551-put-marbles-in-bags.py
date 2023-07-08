class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        
        partition_bars = []
        for i, weight in enumerate(weights):
            if i==0: continue
            partition_bars.append(weights[i]+weights[i-1])
            
        partition_bars.sort()
        
        max_sum = sum(partition_bars[len(partition_bars)-k+1:])
        min_sum = sum(partition_bars[:k-1])
        
        return max_sum - min_sum