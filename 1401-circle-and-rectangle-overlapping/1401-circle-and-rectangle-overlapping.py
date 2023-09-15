class Solution:
    def checkOverlap(self, radius: int, xC: int, yC: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x1 <= xC <= x2 and y1 <= yC <= y2:
            return True
        
        corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
        for x, y in corners:
            if (x - xC) ** 2 + (y - yC) ** 2 <= radius ** 2:
                return True
        
        if x1 <= xC <= x2:
            if abs(yC - y1) <= radius or abs(yC - y2) <= radius:
                return True
        
        if y1 <= yC <= y2:
            if abs(xC - x1) <= radius or abs(xC - x2) <= radius:
                return True
        
        return False
