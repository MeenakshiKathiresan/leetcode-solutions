class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # count number of disconnected 
        # 4, 2, 1
        # [4 2 1]
        
        graph = {}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
                
            if edge[1] not in graph:
                graph[edge[1]] = []
            
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        def dfs(i, size):
            if i not in graph: return 1
            
            if i not in visited:
            
                visited.add(i)
                size = 1

                for node in graph[i]:
                    size += dfs(node, size)

                return size
            else:
                return 0
        
        visited = set()
        output = 0
        remain = n
        for i in range(n):
            if i not in visited:
                size = dfs(i,1)
                output += size * (remain - size)
                remain -= size
             
        return output