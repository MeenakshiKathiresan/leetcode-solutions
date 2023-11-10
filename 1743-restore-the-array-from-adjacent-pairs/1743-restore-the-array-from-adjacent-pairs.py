class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = {}
        
        # 1: 2
        # 2: 1, 3
        # 3: 4, 2
        # 4: 3
        res = []
        for pair in adjacentPairs:
            n1, n2 = pair
            if n1 not in graph:
                graph[n1] = []
            if n2 not in graph:
                graph[n2] = []
            
            graph[n1].append(n2)
            graph[n2].append(n1)
            
        for k, v in graph.items():
            if len(v) == 1:
                start = k
                break
        
        
        def dfs(curr, prev):
            res.append(curr)
            for neighbor in graph[curr]:
                if neighbor != prev:
                    dfs(neighbor, curr)
        dfs(start, None)
        
        return res
            
            
            
        
