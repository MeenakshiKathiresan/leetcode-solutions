from collections import defaultdict
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
      
        if len(connections) < n-1:
            return -1
        
        def dfs(i):
            if i in visited: return 
            visited.add(i)
            for node in graph[i]:
                dfs(node)
        
        extra_cables = 0
        graph = defaultdict(list)
        
        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)
            
        
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
                
        return count - 1
                