class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        # first iteration through the tree - re assign parents
        # second iteration - construct answer

        pos = {}

        
        def construct_graph(parent_list):
            graph = defaultdict(list)
            for i, p in enumerate(parent_list):
                if p != -1:
                    graph[p].append(i) 
            return graph

        graph = construct_graph(parent)
        def dfs(n, pos):
            prev = pos.get(s[n], None)
            if n != 0 and prev is not None:
                parent[n] = prev  

            pos[s[n]] = n  

            for child in graph[n]:
                dfs(child, pos)

            if prev is not None:
                pos[s[n]] = prev
            else:
                del pos[s[n]]
        
        dfs(0, pos)
        graph = construct_graph(parent)

        self.res = [0] * len(s)
        def dfs_child_count(n):
            count = 0
            for child in graph[n]:
                count += dfs_child_count(child)
            self.res[n] = count + 1
            return count + 1

        dfs_child_count(0)
        return self.res

        
        

            
     