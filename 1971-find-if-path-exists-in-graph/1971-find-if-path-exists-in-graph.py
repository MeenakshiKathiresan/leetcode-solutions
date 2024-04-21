class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        
        def convertToGraph(edges):
            graph = {}
            
            for edge in edges:
                if edge[0] not in graph: graph[edge[0]] = []
                if edge[1] not in graph: graph[edge[1]] = []
                
                graph[edge[0]].append(edge[1])
                graph[edge[1]].append(edge[0])
                
            return graph
                
        graph = convertToGraph(edges)
        
        visited = set([source])
        
        queue = deque([source])
        
        while queue:
            current = queue.popleft()
            if current == destination:
                return True
            
            for neigh in graph[current]:
                if neigh not in visited:
                    queue.append(neigh)
                    visited.add(neigh)
        
        
        
        return False