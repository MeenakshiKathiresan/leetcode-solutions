class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        
        graph = {}
        for course, prereq in prerequisites:
            if prereq not in graph:
                graph[prereq] = []
            graph[prereq].append(course)
        
        visited = set()
        visiting = set()
        
        def dfs(prereq):
            if prereq in visiting:
                return False
            
            if prereq in visited:
                return True
            
            visiting.add(prereq)
            
            if prereq in graph:
                for course in graph[prereq]:
                    if not dfs(course):
                        return False
            
            visiting.remove(prereq)
            visited.add(prereq)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
