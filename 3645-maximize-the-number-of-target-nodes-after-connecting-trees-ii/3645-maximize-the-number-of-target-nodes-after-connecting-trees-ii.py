class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        # get the max of tree 2, skip first and get second
        # from root => dp => keep storing 
        # start from any leaf node
        # keep accumulating to alternate - 0 and 1
        # from tree 2 - get value of accumulated 1
        # need to know if its in odd depth or even depth
        n = len(edges1) + 1
        m = len(edges2) + 1

        graph1 = defaultdict(list)
        graph2 = defaultdict(list)

        for edge in edges1:
            graph1[edge[0]].append(edge[1])
            graph1[edge[1]].append(edge[0])
        
        
        for edge in edges2:
            graph2[edge[0]].append(edge[1])
            graph2[edge[1]].append(edge[0])
        
        def bfs(graph):
            visited = set()
            queue = deque([0])
            even_count, odd_count = 0, 0
            curr_count = 0
            while queue:
                queue_len = len(queue)
                for i in range(queue_len):
                    curr = queue.popleft()
                    if curr_count % 2 == 0:
                        even_count += 1
                    else:
                        odd_count += 1
                    visited.add(curr)
                    for neigh in graph[curr]:
                        if neigh not in visited:
                            queue.append(neigh)
                curr_count += 1
            return [even_count, odd_count]

        g2_node_count = max(bfs(graph2))
        g1_node_counts = bfs(graph1)
        
        res = [g2_node_count] * n

        visited = set()
        queue = deque([0])
        curr_count = 0
        while queue:
            queue_len = len(queue)
            for i in range(queue_len):
                curr = queue.popleft()
                if curr_count % 2 == 0:
                    res[curr] += g1_node_counts[0]
                else:
                    res[curr] += g1_node_counts[1]
                visited.add(curr)
                for neigh in graph1[curr]:
                    if neigh not in visited:
                        queue.append(neigh)
            curr_count += 1

        return res

    
                