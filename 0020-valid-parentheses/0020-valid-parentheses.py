class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []
        pairs = {
            "(": ")",
            "[": "]",
            "{":"}"
        }

        for ch in s:
            if ch in pairs:
                bracket_stack.append(ch)
            else:
                if bracket_stack:
                    prev = bracket_stack.pop()
                    if ch != pairs[prev]:
                        return False
                else:
                    return False
        
        return True if not bracket_stack else False
