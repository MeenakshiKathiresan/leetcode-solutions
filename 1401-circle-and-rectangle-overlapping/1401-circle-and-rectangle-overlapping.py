class Solution:
    def checkOverlap(self, radius: int, xC: int, yC: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # if distance between either of the 4 points to the center of the
        # circle is less than radius -> over lap
        
        # or
        
        # center +- radius in x
        # center +- radius in y
        # if they are within the edges (inclusive)
        
        if x1 <= xC <= x2 and y1 <= yC <= y2:
            return True
        
        corners = [[x1,y1],[x1,y2],[x2,y2],[x2,y1]]
        
        def distance(p1x, p1y, p2x, p2y):
            dist = pow(pow(p2x - p1x,2) +  pow(p2y -p1y,2), 0.5)
            return dist
        
        for x,y in corners:
            curr_dist = distance(x,y, xC, yC)
            if curr_dist <= radius:
                return True
                       
                     
        if x1 <= xC <= x2:
            if abs(yC - y1) <= radius or abs(yC - y2) <= radius:
                return True

        if y1 <= yC <= y2:
            if abs(xC - x1) <= radius or abs(xC - x2) <= radius:
                return True
        return False
            
            