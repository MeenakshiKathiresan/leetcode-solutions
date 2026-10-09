class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        close_to_add = 0
        i = 0

        while i < len(s):
            ch = s[i]

            if ch == "(":
                if close_to_add % 2 == 1:
                    res += 1
                    close_to_add -= 1

                close_to_add += 2

            else:
                close_to_add -= 1

                if close_to_add < 0:
                    res += 1
                    close_to_add = 1

            i += 1

        return res + close_to_add