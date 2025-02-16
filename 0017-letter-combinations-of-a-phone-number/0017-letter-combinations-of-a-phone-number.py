class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        """
            first add all characters of first digit
            pop that and add it temp
            for all in the next digit, add that 

        """
        if len(digits) == 0: return []

        d_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7":"pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": " "
        }

        res = []

        def dfs(i, curr):
            if i == len(digits):
                res.append(curr)
            else:
                for ch in d_map[digits[i]]:
                    curr += ch
                    dfs(i + 1, curr)
                    curr = curr[:-1]
        dfs(0, "")
        return res
