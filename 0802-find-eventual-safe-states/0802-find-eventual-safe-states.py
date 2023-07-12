class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n
        adj = [[] for _ in range(n)]
        q = deque()

        for i in range(n):
            indegree[i] = len(graph[i])
            if indegree[i] == 0:
                q.append(i)
            for node in graph[i]:
                adj[node].append(i)

        safeNodes2 = []
        while q:
            node = q.popleft()
            safeNodes2.append(node)

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return sorted(safeNodes2)