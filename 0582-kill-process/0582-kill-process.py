class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        
        # graph:
        #     1 : 
        #     3 : [1, 5]
        #     10 : 
        #     5 : [10]
                
        graph = {}
        graph[0] =[]
        
        for p in pid:
            graph[p] = []
        
        for i, p in enumerate(ppid):
            graph[p].append(pid[i])
            
        res = [kill]
        queue = [kill]
        
        while queue:
            curr = queue.pop(0)
            
            for child in graph[curr]:
                res.append(child)
                queue.append(child)
                
        return res