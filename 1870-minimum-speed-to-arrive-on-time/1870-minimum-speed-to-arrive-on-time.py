class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        if len(dist) > ceil(hour):
            return -1
        
        l, r = 1, 10000000
        
        min_speed = -1
        
        while l <= r:
            
            speed = (l+r)/2
            
            total_time = 0
            for i, dis in enumerate(dist):
                time = float(dis)/float(speed)
                if i == len(dist)-1:
                    total_time += time
                else:
                    total_time += ceil(time)
            
            if total_time > hour:
                l = speed + 1
            else:
                r = speed - 1
                min_speed = speed
           
            
        return min_speed