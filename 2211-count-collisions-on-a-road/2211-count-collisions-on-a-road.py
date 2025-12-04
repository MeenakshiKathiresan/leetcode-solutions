class Solution:
    def countCollisions(self, directions: str) -> int:
        # left to right;
        # right to left;

        # find left most right and right most left
        # left to right, add all right before right most left
        # right to left, add all left after 
        lm_right = len(directions)
        rm_left = -1

        for i, d in enumerate(directions):
            if d != "L" and i < lm_right:
                lm_right = i
            elif d != "R" and i > rm_left:
                rm_left = i
    
        res = 0
        for i, d in enumerate(directions):
            if d == "R" and i <= rm_left:
                res += 1
            elif d == "L" and i >= lm_right:
                res += 1
        return res
        
        