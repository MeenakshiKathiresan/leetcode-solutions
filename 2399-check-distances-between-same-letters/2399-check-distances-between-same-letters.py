class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dist = {}
        
        
        for i, ch in enumerate(s):
            if ch not in dist:
                dist[ch] = []
            dist[ch].append(i)
        
        for i, d in enumerate(distance):
            key = chr(97 + i)
            
            if key in dist and dist[key][1]-dist[key][0]-1!= d:
                return False
        return True
            