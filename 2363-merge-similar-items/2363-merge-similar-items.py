class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        value_weight = {}
        
        for item in items1:
            if item[0] not in value_weight:
                value_weight[item[0]] = 0
            value_weight[item[0]] += item[1]
        
        for item in items2:
            if item[0] not in value_weight:
                value_weight[item[0]] = 0
            value_weight[item[0]] += item[1]
            
        
        return sorted([[value, weight] for value, weight in value_weight.items()])
        