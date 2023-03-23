from collections import defaultdict
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # find total number of unconnected units
        """
        0: [1,2]
        1: [0,2]
        2: [0,1]
        """
        
        # construct adjacency list
        
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
            
            extra_cables += min(len(graph[a]), len(graph[b])) - 1
        
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        print(count)
        print(extra_cables, graph)
                
        if extra_cables < count -1: return -1
        return count - 1
                