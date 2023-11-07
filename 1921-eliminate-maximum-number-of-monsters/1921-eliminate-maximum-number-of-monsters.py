class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
#         based on dist and speed
#         we can have time to reach array
        
#         time taken = [0.6, 0.66, 2]
        
        time = []
        
        for i in range(len(dist)):
            time.append(dist[i]/speed[i])
        
        
        time.sort()
        print(time)
        
        
        last = time[0]
        i = 1
        
        while i < len(time) and (time[i] - last >= 1 or time[i] > i):
            last = time[i]
            i += 1
          
            
        return i
            
        
        