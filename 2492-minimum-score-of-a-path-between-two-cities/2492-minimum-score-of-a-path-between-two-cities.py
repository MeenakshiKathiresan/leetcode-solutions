
from collections import defaultdict
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
#         1: [ (2,9) (4,7) ]
#         2: [ (1,9) (3,6) (4,5)]
#         3: [ (2,6) ]
#         4: [ (1,7) (2,5)]
            
#         1 -> 4 - dist 7
#         1 -> 2 -> 3 NA
#              2 -> 4 dist min(9,5) -> 5


        # construct adjacency list
        road_graph = defaultdict(list)
        
        for road in roads:
            road_graph[road[0]].append((road[1],road[2]))
            road_graph[road[1]].append((road[0],road[2]))
        
      
        shortest = 10000
        queue = deque([(1,shortest)])
        visited = set()
        
        while queue:
            current = queue.pop()
            
            #if current[0] == n-1:
                # check if its lower than shortest and update shortest
                # dont add anthing to queue
            if current[1] < shortest:
                shortest = current[1]
                
            if current[0] not in visited:
                visited.add(current[0])
                
                for road in road_graph[current[0]]:
                    queue.append((road[0], min(road[1],current[1])))
                    
        return shortest
                
                
                