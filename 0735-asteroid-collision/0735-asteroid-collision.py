class Solution(object):
    
    res = []
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        ans = []
        
        
        for i, asteroid in enumerate(asteroids):
            if i == 0: 
                ans.append(asteroids[i])
                continue
                
            if len(ans) > 0 and ans[-1] > 0 and asteroids[i] < 0:
                prev = ans.pop()
                
                if abs(prev) > abs(asteroids[i]):
                    curr = prev
                    
                elif abs(prev) < abs(asteroids[i]):
                    curr = asteroids[i]
                else:
                    continue
                
                ans.append(curr)
                
            else:
                ans.append(asteroids[i])
        
        if self.res == ans:
            return ans
        else:
            self.res = ans
            return self.asteroidCollision(self.res)
        