class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        # at each step find highest val below mass
        
        for a in sorted(asteroids):
            if mass < a:
                return False
            mass += a
        return True