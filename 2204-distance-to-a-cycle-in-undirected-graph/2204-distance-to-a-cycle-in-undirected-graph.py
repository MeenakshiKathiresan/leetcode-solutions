from collections import defaultdict
class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        
        res = [n] * n
        
        g = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        
        # step 1: backtracking DFS to find the cycle
        circle = []
        vis = set()
        
        def find_circle(node, par):
            if node in vis:
                return (True, node)
            for nei in g[node]:
                if nei == par: continue
                vis.add(node)
                circle.append(node)
                status, res = find_circle(nei, node)
                if status: return status, res
                circle.pop()
                vis.remove(node)

            return False, None

        
        _, node = find_circle(0, None)
        circle = circle[circle.index(node):] 
        
        
        queue = deque()
        cycle_set = set(circle)
        
        for item in cycle_set:
            queue.append((item, 0))
            
        
        visited = set()
        while queue:
            curr, dist = queue.popleft()
            visited.add(curr)
            
            res[curr] = min(res[curr], dist)
            
            for neigh in g[curr]:
                if neigh not in visited:
                    queue.append((neigh, dist +1))
        
        
        return res
