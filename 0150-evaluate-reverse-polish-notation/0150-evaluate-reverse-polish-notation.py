class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []

        for token in tokens:
            if token in ["+", "-","/", "*"] and len(num_stack) > 1:
                n2 = num_stack.pop()
                n1 = num_stack.pop()
                res = 0
                if token == "+":
                    res = n1 + n2
                elif token == "-":
                    res = n1 - n2
                elif token == "*":
                    res = n1 * n2
                else:
                    res = int(n1/n2)
                num_stack.append(res)
            else:
                num_stack.append(int(token))
        return num_stack[0]
