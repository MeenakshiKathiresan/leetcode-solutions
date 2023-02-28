class Solution:
    org_color = None
    image = None
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        self.org_color = image[sr][sc]
        self.image = image
        
        if self.image[sr][sc]!=color:
            return self.fill(sr,sc, color)
        else:
            return self.image
        
    
    def fill(self, sr: int, sc: int, color:int):
        self.image[sr][sc] = color
            
        neighbors = [(sr+1,sc), (sr-1,sc), (sr,sc+1), (sr, sc-1)]
        
        for neighbor in neighbors:
            if neighbor[0]>= 0 and neighbor[0] < len(self.image) and neighbor[1] >=0  and neighbor[1] < len(self.image[0]):
                if self.image[neighbor[0]][neighbor[1]] == self.org_color:
                    self.fill(neighbor[0], neighbor[1], color)
   
        
        return self.image
        
        