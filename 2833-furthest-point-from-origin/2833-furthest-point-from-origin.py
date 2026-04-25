class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        L_count = 0
        R_count = 0
        D_count = 0

        for move in moves:
            if move == "L":
                L_count += 1
            elif move == "R":
                R_count += 1
            else:
                D_count += 1
        
        if L_count > R_count:
            return L_count - R_count + D_count
        else:
            return R_count - L_count + D_count
