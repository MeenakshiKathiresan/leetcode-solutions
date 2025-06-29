class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        At each step - either close if we have or create new
        Create one -> open new or close existing

        if we got all the brackets return res
        """

        res = []
        def recurse(left, stack, curr):
            if left == 0:
                while stack:
                    curr += ")"
                    stack -= 1
                res.append(curr)
                return
            
            if left > 0:
                recurse(left - 1, stack + 1, curr + "(")
            
            if stack > 0:
                recurse(left, stack - 1, curr + ")")
            
        
        recurse(n, 0, "")
        return res
            
            