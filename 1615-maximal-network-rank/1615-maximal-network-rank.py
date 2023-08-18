class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        graph = {}
        
        for i in range(n):
            graph[i] = []
        
        for road in roads:
            
            graph[road[0]].append(road[1])
            graph[road[1]].append(road[0])
            
        max_rank = 0
        for n1 in range(n):
            for n2 in range(n1+1, n):
                rank = len(graph[n1]) + len(graph[n2])
                
                if n1 in graph[n2]:
                    rank -= 1
                
                max_rank = max(max_rank, rank)
        return max_rank
            
        