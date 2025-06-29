class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recurse(left, right, curr):
            if left == right == n:
                res.append(curr)
                return
            if left < n:
                recurse(left + 1, right, curr + "(")
            if right < left:
                recurse(left, right + 1, curr + ")")

        recurse(0, 0, "")
        return res
