class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        
        
        
        graph = {}
        
        for i, edge in enumerate(edges):
            if edge[0] not in graph:
                graph[edge[0]] = []
            if edge[1] not in graph:
                graph[edge[1]] = []
            graph[edge[0]].append([edge[1], succProb[i]])
            graph[edge[1]].append([edge[0],succProb[i]])
        
        
        queue = deque([(start)])
        
        max_prob = [0.0] * n    
        max_prob[start] = 1.0
        
        res = 0
        
        while queue:
            
            curr_node = queue.popleft()
            
            
            if curr_node in graph:
                
                for neigh, neigh_pb in graph[curr_node]:
                    if max_prob[curr_node] * neigh_pb > max_prob[neigh]:
                        max_prob[neigh] = max_prob[curr_node] * neigh_pb
                        queue.append(neigh)
                
            
        return max_prob[end]