class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        available_groups = {}
        res = []
        
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            if size not in available_groups:
                available_groups[size] = []
            
            available_groups[size].append(i)
            if len(available_groups[size]) == size:
                res.append(available_groups[size])
                available_groups[size] = []
        return res