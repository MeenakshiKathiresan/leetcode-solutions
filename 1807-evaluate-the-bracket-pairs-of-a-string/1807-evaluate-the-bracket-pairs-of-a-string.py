class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        knowledge_map = {}
        for k in knowledge:
            knowledge_map[k[0]] = k[1]
        
        res = []
        i, j = 0, 0
        while i < len(s):
            if s[i] == "(":
                j = s.find(")",i)
                res.append(knowledge_map.get(s[i + 1:j], "?"))
                i = j + 1
            else:
                res.append(s[i])
                i += 1
        return "".join(res)
