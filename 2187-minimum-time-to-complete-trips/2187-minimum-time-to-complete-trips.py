class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        # range 1 to max of time
        # binary search through it
        
        left = 1
        right = min(time) * totalTrips
        
        while left <= right:
            mid = (left + right)//2
            
            total = 0
            
            for t in time:
                total += mid//t
            
            print(mid, total)
            
            if total < totalTrips:
                left = mid + 1
            else:
                right = mid - 1
           
            
        return left
        
                