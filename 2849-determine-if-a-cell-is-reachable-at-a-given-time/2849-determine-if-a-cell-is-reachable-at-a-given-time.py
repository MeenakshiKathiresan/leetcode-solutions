class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        current_t = 0
        
        if sx == fx and sy == fy:
            if t == 1:
                return False
            else:
                return True
        
        if abs(sx - fx) <= t and abs(sy -fy) <= t:
            return True
        return False