class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # open then open - skip
        open = 0
        res = []
        for ch in s:
            if ch == "(":
                if open != 0:
                    res.append(ch)
                open += 1
            else:
                if open != 1:
                    res.append(ch)
                open -= 1
        return "".join(res)
                    