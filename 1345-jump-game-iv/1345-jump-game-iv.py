class Solution:
    def minJumps(self, arr: List[int]) -> int:
    
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = deque([0] )
        visited = {0}
        step = 0
        
        while curs:
            nex = []
            for i in range(len(curs)):
                node = curs.popleft()
                
                if node == n-1:
                    return step

                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        curs.append(child)

                graph[arr[node]].clear()

                for child in [node-1, node+1]:
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        curs.append(child)
            step += 1

        return -1