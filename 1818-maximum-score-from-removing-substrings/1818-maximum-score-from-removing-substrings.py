class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def remove(str_list, first, second, score):
            stack = []
            res = 0
            for ch in str_list:
                if stack and ch == second and stack[-1] == first:
                    res += score
                    stack.pop()
                else:
                    stack.append(ch)

            return stack, res

        if x > y:
            str_list, scoreX = remove(list(s), "a", "b", x)
            _, scoreY = remove(str_list, "b", "a", y)
            return scoreX + scoreY
        else:
            
            str_list, scoreY = remove(list(s), "b", "a", y)
            _, scoreX = remove(str_list, "a", "b", x)
            return scoreX + scoreY
        